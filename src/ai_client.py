from anthropic import Anthropic
from inspeq.client import InspeqEval
from dotenv import load_dotenv
import json, logging, os
from datetime import datetime

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class AIClient:
    """
    A client for interacting with AI services and evaluating responses.

    This class integrates with the Anthropic API for generating responses
    and the Inspeq API for evaluating AI-generated content. It handles
    initialization of API clients, environment variable validation,
    and provides methods for interacting with these services.

    Attributes:
        claude (Anthropic): An instance of the Anthropic API client (not AWS Bedrock).
        inspeq_eval (InspeqEval): An instance of the Inspeq evaluation client.

    Raises:
        Exception: If initialization fails or required environment variables are missing.
    """


class AIClient:
    def __init__(self):
        try:
            # Validate required environment variables
            load_dotenv()
            if not all(
                [
                    os.getenv("CLAUDE_API_KEY"),
                    os.getenv("INSPEQ_API_KEY"),
                    os.getenv("INSPEQ_PROJECT_ID"),
                ]
            ):
                raise Exception("Missing required environment variables")

            self.claude_client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
            self.inspeq_eval = InspeqEval(
                inspeq_api_key=os.getenv("INSPEQ_API_KEY"),
                inspeq_project_id=os.getenv("INSPEQ_PROJECT_ID"),
            )

        except Exception as e:
            logger.error(f"Failed to initialize AIClient: {str(e)}")
            raise Exception(f"Initialization failed: {str(e)}")

    def _save_response(self, response_data) -> None:
        """Save response data to JSON file with timestamp"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"response_{timestamp}.json"

            with open(filename, "a") as f:
                json_data = {"timestamp": timestamp, "data": response_data}
                f.write(json.dumps(json_data) + "\n")

        except Exception as e:
            logger.error(f"Failed to save response: {str(e)}")

    def ask_claude(self, prompt, context):
        """Send request to Claude API with error handling and logging"""
        payload = (
            f"Leverage the context:{context} to execute the following prompt:{prompt}"
        )

        try:
            logger.info("Sending request to Claude API")
            message = self.claude_client.messages.create(
                model="claude-3-5-sonnet-latest",
                # Giving enough space to the context and prompt to fit should
                # they be included in the response as well
                max_tokens=1500,
                messages=[{"role": "user", "content": payload}],
            )
            response = message.content[0].text
            logger.info("Successfully received response from Claude")
            return response

        except Exception as e:
            logger.error(f"Claude API error: {str(e)}")
            return None

    def evaluate_prompt(
        self,
        prompt: str,
        context=None,
        metrics=None,
    ):
        """Evaluate prompt with InspeqAI"""
        try:
            logger.info("Sending initial prompt evaluation to Inspeq")
            input_data = [
                {
                    "prompt": prompt,
                    "response": "",
                    "context": context or "",
                }
            ]

            results = self.inspeq_eval.evaluate_llm_task(
                metrics_list=metrics,
                input_data=input_data,
                task_name="prompt_evaluation_v3",
            )
            logger.info("Prompt evaluation completed successfully")
            return results

        except Exception as e:
            logger.error(f"Prompt evaluation failed: {str(e)}")
            return None

    def evaluate_response(
        self,
        prompt,
        response,
        context=None,
        metrics=None,
    ):
        """Evaluate response with InspeqAI"""
        try:
            logger.info("Sending request for response evaluation to Inspeq AI")
            input_data = [
                {
                    "prompt": prompt,
                    "response": response,
                    "context": context or "",
                }
            ]

            results = self.inspeq_eval.evaluate_llm_task(
                metrics_list=metrics,
                input_data=input_data,
                task_name="response_evaluation_v3",
            )
            logger.info("Response evaluation completed successfully")
            return results

        except Exception as e:
            logger.error(f"Response evaluation failed: {str(e)}")
            return None

    def complete_evaluation_flow(
        self,
        prompt,
        context=None,
        prompt_metrics=None,
        response_metrics=None,
        max_retries=3,
        retry_delay=1,
    ):
        """Complete flow: evaluate prompt, get Anthropic's Claude response, evaluate response with Inspeq AI"""
        result = {}

        for attempt in range(max_retries):
            try:
                logger.info(f"Starting evaluation flow - Attempt {attempt + 1}")

                # Step 1: Evaluate the prompt
                prompt_evaluation = self._retry_operation(
                    self.evaluate_prompt,
                    prompt=prompt,
                    context=context,
                    metrics=prompt_metrics,
                )
                result["prompt_evaluation"] = prompt_evaluation
                if any(
                    metric.get("metric_evaluation_status") == "FAILED"
                    for metric in prompt_evaluation.get("results", [])
                ):
                    result["failed_metrics"] = True

                # Step 2: Get response from Claude
                claude_response = self._retry_operation(
                    self.ask_claude,
                    prompt,
                    context,
                )
                if not claude_response:
                    raise AIClientError("Failed to get response from Claude")
                result["response"] = claude_response

                # Step 3: Evaluate the response
                response_evaluation = self._retry_operation(
                    self.evaluate_response,
                    prompt=prompt,
                    context=context,
                    response=claude_response,
                    metrics=response_metrics,
                )
                result["response_evaluation"] = response_evaluation
                if any(
                    metric.get("Status") == "FAILED"
                    for metric in response_evaluation.get("results", [])
                ):
                    result["failed_metrics"] = True

                # For bookkeeping, save the complete response locally
                self._save_response(result)
                logger.info("Evaluation flow completed successfully")
                return result

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                else:
                    logger.error("All retry attempts failed")
                    return {
                        "error": str(e),
                        "prompt_evaluation": result.get("prompt_evaluation"),
                        "response": result.get("response"),
                        "response_evaluation": result.get("response_evaluation"),
                    }

    def _retry_operation(self, operation, *args, **kwargs):
        """Helper method to retry operations with exponential backoff"""
        max_retries = kwargs.pop("max_retries", 3)
        for attempt in range(max_retries):
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                wait_time = (2**attempt) + random.uniform(0, 1)
                logger.warning(f"Operation failed, retrying in {wait_time:.2f} seconds")
                time.sleep(wait_time)

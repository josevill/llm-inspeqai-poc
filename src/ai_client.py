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
    def __init__(self):
        load_dotenv()
        try:
            self.claude = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
            self.inspeq_eval = InspeqEval(
                inspeq_api_key=os.getenv("INSPEQ_API_KEY"),
                inspeq_project_id=os.getenv("INSPEQ_PROJECT_ID"),
            )

            # Validate required environment variables
            if not all(
                [
                    os.getenv("CLAUDE_API_KEY"),
                    os.getenv("INSPEQ_API_KEY"),
                    os.getenv("INSPEQ_PROJECT_ID"),
                ]
            ):
                raise Exception("Missing required environment variables")

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
            message = self.claude.messages.create(
                model="claude-3-5-sonnet-latest",
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
            logger.info("Starting prompt evaluation")
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
        prompt: str,
        response: str,
        context=None,
        metrics=None,
    ):
        """Evaluate response with InspeqAI"""
        try:
            logger.info("Starting response evaluation")
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
    ):
        """Complete flow: evaluate prompt, get Claude response, evaluate response"""
        result = {}

        try:
            # Step 1: Evaluate the prompt
            logger.info("Starting evaluation flow - Step 1: Prompt evaluation")
            prompt_evaluation = self.evaluate_prompt(
                prompt=prompt, context=context, metrics=prompt_metrics
            )
            result["prompt_evaluation"] = prompt_evaluation

            # Step 2: Get response from Claude
            logger.info("Starting evaluation flow - Step 2: Claude request")
            claude_response = self.ask_claude(prompt, context)
            if not claude_response:
                raise AIClientError("Failed to get response from Claude")
            result["response"] = claude_response

            # Step 3: Evaluate the response
            logger.info("Starting evaluation flow - Step 3: Response evaluation")
            response_evaluation = self.evaluate_response(
                prompt=prompt,
                context=context,
                response=claude_response,
                metrics=response_metrics,
            )
            result["response_evaluation"] = response_evaluation

            # For bookkeeping, save the complete response locally
            self._save_response(result)
            logger.info("Evaluation flow completed successfully")

            return result

        except Exception as e:
            logger.error(f"Evaluation flow failed: {str(e)}")
            return {
                "error": str(e),
                "prompt_evaluation": result.get("prompt_evaluation"),
                "response": result.get("response"),
                "response_evaluation": result.get("response_evaluation"),
            }

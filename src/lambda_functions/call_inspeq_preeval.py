import os
from inspeq.client import InspeqEval

# Initialize the client
INSPEQ_API_KEY = os.environ.get("INSPEQA")
INSPEQ_PROJECT_ID = os.environ.get("INSPEQB")

inspeq_eval = InspeqEval(
    inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID
)


def lambda_handler(event, context):
    input_data = [{"prompt": event.get("prompt"), "context": event.get("context")}]

    metrics_list = ["DATA_LEAKAGE"]

    results = None
    try:
        results = inspeq_eval.evaluate_llm_task(
            metrics_list=metrics_list,
            input_data=input_data,
            task_name="question_from_lambda_v2",
        )
        print(results)

        if results is not None:
            return {
                "statusCode": results.get("status"),
                "body": {
                    "prompt": event.get("prompt"),
                    "context": event.get("context"),
                    "passed": results.get("results")[0].get("passed"),
                    "results": results.get("results")[0].get("evaluation_details"),
                },
            }
        else:
            return {
                "statusCode": 400,
                "body": "Error, enable further debugging and troubleshoot in your Lambda function",
            }
    except Exception as e:
        print(f"An error occurred: {str(e)}")

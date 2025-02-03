import json, os
from inspeq.client import InspeqEval

# Initialize the client
INSPEQ_API_KEY = os.environ.get("INSPEQA")
INSPEQ_PROJECT_ID = os.environ.get("INSPEQB")

inspeq_eval = InspeqEval(
    inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID
)


def lambda_handler(event, context):
    input_data = [
        {
            "prompt": event.get("prompt"),
            "context": event.get("context"),
            "response": event.get("llm_response"),
        }
    ]

    metrics_list = ["RESPONSE_TONE"]

    results = None
    try:
        results = inspeq_eval.evaluate_llm_task(
            metrics_list=metrics_list,
            input_data=input_data,
            task_name="eval_question_from_lambda_v2",
        )
        print(results)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}

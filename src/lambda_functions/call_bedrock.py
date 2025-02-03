import boto3, json, os

client = boto3.client("bedrock-runtime")


def lambda_handler(event, context):
    prompt = event.get("prompt", "")
    user_context = event.get("context", "")
    results = event.get("results", "")

    guardrail_identifier = event.get("guardrailIdentifier", "")
    guardrail_version = event.get("guardrailVersion", "")

    formatted_prompt = f"""
    System: Use the following context to help frame your response: {user_context}

    Human: {prompt}

    Assistant:
    """

    try:

        response = None
        if guardrailIdentifier and guardrailVersion:
            response = client.invoke_model(
                modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
                guardrailIdentifier=guardrail_identifier,
                guardrailVersion=guardrail_version,
                body=json.dumps(
                    {
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": 4096,
                        "messages": [{"role": "user", "content": formatted_prompt}],
                    }
                ),
            )
        else:
            response = client.invoke_model(
                modelId="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
                body=json.dumps(
                    {
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": 4096,
                        "messages": [{"role": "user", "content": formatted_prompt}],
                    }
                ),
            )
        response_body = json.loads(response["body"].read())
        print(response_body)

        return {
            "statusCode": 200,
            "body": {
                "prompt": prompt,
                "context": user_context,
                "llm_response": response_body["content"][0]["text"],
                "results": results,
            },
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {
                "error": f"Error calling Bedrock: {str(e)}",
                "prompt": prompt,
                "context": user_context,
            },
        }

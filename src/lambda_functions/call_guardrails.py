import boto3, json, os

client = boto3.client("bedrock")


def lambda_handler(event, context):
    try:
        create_response = client.create_guardrail(
            name="remove-pii-workflow",
            description="Prevents the our model from output of any possible PII thats being passed.",
            sensitiveInformationPolicyConfig={
                "piiEntitiesConfig": [
                    {"type": "EMAIL", "action": "ANONYMIZE"},
                    {"type": "PHONE", "action": "ANONYMIZE"},
                    {"type": "NAME", "action": "ANONYMIZE"},
                ]
            },
            blockedInputMessaging="""I can provide general info about Acme Financial's products and services, but can't fully address your request here. For personalized help or detailed questions, please contact our customer service team directly. For security reasons, avoid sharing sensitive information through this channel. If you have a general product question, feel free to ask without including personal details. """,
            blockedOutputsMessaging="""I can provide general info about Acme Financial's products and services, but can't fully address your request here. For personalized help or detailed questions, please contact our customer service team directly. For security reasons, avoid sharing sensitive information through this channel. If you have a general product question, feel free to ask without including personal details. """,
            tags=[
                {"key": "purpose", "value": "anonymize-pii"},
            ],
        )

        version_response = client.create_guardrail_version(
            guardrailIdentifier=create_response["guardrailId"],
            description="Version of Guardrail",
        )

        return {
            "statusCode": 200,
            "body": {
                "guardrailIdentifier": create_response["guardrailId"],
                "guardrailVersion": version_response["version"],
            },
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": {
                "error": f"Error calling Bedrock: {str(e)}",
            },
        }

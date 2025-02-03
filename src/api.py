from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import boto3
import json
from ai_client import AIClient

app = FastAPI(title="Blog Generator API")
ai_client = AIClient()


class BlogRequest(BaseModel):
    prompt: str
    context: str | None = None
    prompt_metrics: list | None = None
    response_metrics: list | None = None


class InvokeRequest(BaseModel):
    prompt: str
    context: str | None = None


client = boto3.client("stepfunctions")
step_function_arn = (
    "arn:aws:states:us-east-1:XXXXXXXXXXXX:stateMachine:MyStateMachine-obrluyueo"
)


# Invoke this endpoint with:
# curl -X POST "http://localhost:8000/invoke" -H "Content-Type: application/json" -d '{"prompt": "Your prompt here", "context": "Optional context here"}'
###
# curl -X POST "http://localhost:8000/invoke" \
#      -H "Content-Type: application/json" \
#      -d '{
#   "prompt": "Generate a blog post for our reinsurance company. It needs to be on things related to our profiles and what is to come in the FSI sector for 2025, things like regulations, market trends, market shares or industry standards that are coming into action for the new year. Leverage the context to tailor the output as closer to the needs of the target audience, keep in mind the Profiles in the context to create the title and paragraphs of the blog post. Explain any concept in simple terms, if there is the need to use complex jargon of the industry or overall, explain it in a sentence or two. If you use any acronyms, explain them in a sentence with the full name. If you use any word that is only used in the industry, make sure to explain it as well. Keep the technicallity of the output as simple as possible as anyone from within the industry must be able to understand the content, consume it and assimilate it for it to be engaging. Use the context to build this blog post based on the locations of the profiles, target audiences and their key markets. Keep in mind the average word count for the output up to the ranges provided by the profiles. Dont make any assumptions over topics you are not quiet aware or have little to no knowledge about. Make references to the profiles, target audiences and their key markets, things like '\''how Bank X is could tackle Y problem in 2025'\'' for example. Do not include any odd character or empty characters besides spaces and newlines.",
#   "context": "We are a reinsurance company, you have the knowledge of the following profiles that consume our content and potentially our services:\nTraditional Bank Profile:\nInstitution: FinoBank AG\nLocation: Frankfurt, Germany\nType: Traditional Banking Institution\nKey Markets: Germany, Austria, Switzerland\nTarget Audience: Retail investors, Wealth management clients\nRegulatory Framework: EU Banking Union, MiFID II\nTechnical Level: Intermediate\nWord Count Range: 1500 words\n---\nFintech Company Profile:\nInstitution: NeoFinance SAS\nLocation: Paris, France\nType: Digital Financial Services Provider\nKey Markets: France, Benelux countries\nTarget Audience: Tech-savvy investors, Digital natives\nRegulatory Framework: EU MiCA, PSD3\nTechnical Level: Advanced\nWord Count Range: 1200~1800 words"
# }'
###


@app.post("/invoke")
async def invoke(request: InvokeRequest):
    """
    Invoke the step function execution with the provided prompt and context.

    Example:
    curl -X POST "http://localhost:8000/invoke" \
     -H "Content-Type: application/json" \
     -d '{
  "prompt": "Generate a blog post for our reinsurance company. It needs to be on things related to our profiles and what is to come in the FSI sector for 2025, things like regulations, market trends, market shares or industry standards that are coming into action for the new year. Leverage the context to tailor the output as closer to the needs of the target audience, keep in mind the Profiles in the context to create the title and paragraphs of the blog post. Explain any concept in simple terms, if there is the need to use complex jargon of the industry or overall, explain it in a sentence or two. If you use any acronyms, explain them in a sentence with the full name. If you use any word that is only used in the industry, make sure to explain it as well. Keep the technicallity of the output as simple as possible as anyone from within the industry must be able to understand the content, consume it and assimilate it for it to be engaging. Use the context to build this blog post based on the locations of the profiles, target audiences and their key markets. Keep in mind the average word count for the output up to the ranges provided by the profiles. Dont make any assumptions over topics you are not quiet aware or have little to no knowledge about. Make references to the profiles, target audiences and their key markets, things like '\''how Bank X is could tackle Y problem in 2025'\'' for example. Do not include any odd character or empty characters besides spaces and newlines.",
  "context": "We are a reinsurance company, you have the knowledge of the following profiles that consume our content and potentially our services:\nTraditional Bank Profile:\nInstitution: FinoBank AG\nLocation: Frankfurt, Germany\nType: Traditional Banking Institution\nKey Markets: Germany, Austria, Switzerland\nTarget Audience: Retail investors, Wealth management clients\nRegulatory Framework: EU Banking Union, MiFID II\nTechnical Level: Intermediate\nWord Count Range: 1500 words\n---\nFintech Company Profile:\nInstitution: NeoFinance SAS\nLocation: Paris, France\nType: Digital Financial Services Provider\nKey Markets: France, Benelux countries\nTarget Audience: Tech-savvy investors, Digital natives\nRegulatory Framework: EU MiCA, PSD3\nTechnical Level: Advanced\nWord Count Range: 1200~1800 words"
}'
    Args:
        request (InvokeRequest): An object containing the prompt and optional context.

    Returns:
        dict: A dictionary containing the status and execution ARN.

    Raises:
        HTTPException: If there's an error during the execution.
    """
    try:
        payload = {
            "prompt": request.prompt,
            "context": request.context if request.context is not None else "",
        }
        response = client.start_execution(
            stateMachineArn=step_function_arn, input=json.dumps(payload)
        )
        return {"status": "success", "execution_arn": response["executionArn"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate")
async def generate_blog(request: BlogRequest):
    try:
        result = ai_client.complete_evaluation_flow(
            prompt=request.prompt,
            context=request.context,
            prompt_metrics=request.prompt_metrics,
            response_metrics=request.response_metrics,
        )
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/evaluate-prompt")
async def evaluate_prompt(request: BlogRequest):
    try:
        result = ai_client.evaluate_prompt(
            prompt=request.prompt,
            context=request.context,
            metrics=request.prompt_metrics,
        )
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-content")
async def generate_content(request: BlogRequest):
    try:
        result = ai_client.ask_claude(prompt=request.prompt, context=request.context)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

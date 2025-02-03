# Inspeq AI & Anthropic PoC (local)

This project provides a Python interface to interact with Claude AI for content generation and InspeqAI for content evaluation. It includes a complete workflow for evaluating prompts, generating content, and evaluating responses.

## Features

- Content generation using the latest version of Anthropic's Claude Sonnet 3.5 from their API
- Prompt & Response evaluation using InspeqAI
- Automatic response logging and tracking
- Comprehensive error handling and logging

## Prerequisites

- Python 3.12, the packages under the requirements.txt file may be compatible with older versions of Python.
- [Anthropic API](https://docs.anthropic.com/)
- [Anthropic API Key](https://console.anthropic.com/)
- [InspeqAI API Key and Project ID](https://inspeq.ai/)

## Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:josevill/llm-inspeqai-poc.git
   cd llm-inspeqai-poc
   ```

2. To keep your environment clean, create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a copy of `.env.example` as `.env` file in the project root and fill it with your credentials:
   ```env
   CLAUDE_API_KEY=your_claude_api_key
   INSPEQ_API_KEY=your_inspeq_api_key
   INSPEQ_PROJECT_ID=your_inspeq_project_id
   ```

## Usage

### Running the Project (AWS)
Create the functions as per all the functions provided under `src/lambda_functions/`
You will need all necesarry permissions to run the functions as they call on Bedrocks API and will most likely need to read and write logs to CloudWatch, the default role created by the Lambda API will suffice yet for Bedrock given certain scenario, you will need to call the Guardrails endpoint and the Invoke endpoint for Bedrock.

Your mileage might vary, yet the following policy should suffice for this end:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BedrockAll",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:createGuardrail",
                "bedrock:CreateGuardrailVersion",
            ],
            "Resource": "*"
        }
    ]
}

You will also need to create two environment variables into your lambdas, INSPEQAPI and INSPEQPROJECT.
Which you can define in the configuration panel under the Lambda Functions call_inspeq_*.
Keep in mind that given the nature of this workload, you will also need to increase the Timeout periods for your lambdas that interact with Bedrock for Inference as generation of content can take some time, several trials led to have a sweet spot around a minute and minute and a half of timeout span for your functions to generate the content, so feel free to modify the time for those.

Once everything is in place, go to the main folder in your environment and run your API to interface with your step function state machine.
You will need to configure the state machine ARN in your code `src/api.py`:
```python
step_function_arn = (
    "arn:aws:states:us-east-1:<account-id>:stateMachine:state_machine_name"
)
```
If you are using a different region, you will need to change the region to the one you are using as well.

```
### Running the Project (Local)

```bash
python src/main.py
```
### In case of wanting to use Bedrock instead of Anthropic's API directly
You can make the following change to the ai_client.py file:
```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock()

# Line 1:
# From this:
from anthropic import Anthropic
# To this:
from anthropic import AnthropicBedrock

------

# Line 45:
# From this
self.claude_client = Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))
# To this:
self.claude_client = AnthropicBedrock()
# You can also do this:
self.claude_client = AnthropicBedrock(
  aws_profile='...', # Only if profiles are already configured for your account under ~/.aws
  aws_region='...',
  aws_secret_key='...',
  aws_access_key='...',
  aws_session_token='...', # Optional, only needed for temporary credentials
)
------

# Line 76:
# From this
message = self.claude_client.messages.create(
    model="claude-3-5-sonnet-latest",
    max_tokens=1500,
    messages=[{"role": "user", "content": payload}],
)

# To this:
message = self.claude_client.messages.create(
    model="anthropic.claude-3-5-sonnet-20241022-v2:0",
    max_tokens=1500,
    messages=[{"role": "user", "content": payload}],
)


```
Bear in mind that you will have to have credentials already configured for an AWS Account in your desired region where Bedrock is enabled and the Sonnet Model is available.

### Modifying the Prompt and Context

To modify the prompt and context, edit `src/main.py`. Look for these variables:

```python
prompt = """
Generate a blog post for our reinsurance company.
It needs to be on things related to our profiles...
"""

context = """
We are a reinsurance company, you have the knowledge...
"""
```

### Configuring Evaluation Metrics

The project uses two sets of metrics:

1. Prompt Metrics (pre-evaluation):
```python
prompt_metrics = [
    "DATA_LEAKAGE",
    "INSECURE_OUTPUT",
    "COHERENCE",
    "GRAMMATICAL_CORRECTNESS",
    "TOXICITY",
]
```

2. Response Metrics (post-evaluation):
```python
response_metrics = [
    "RESPONSE_TONE",
    "ANSWER_RELEVANCE",
    "FACTUAL_CONSISTENCY",
    "READABILITY",
    "CLARITY",
]
```

Available Inspeq AI metrics include:

- `DATA_LEAKAGE`: Checks for potential data leaks in prompts
- `INSECURE_OUTPUT`: Evaluates security concerns in output
- `COHERENCE`: Measures text coherence and flow
- `GRAMMATICAL_CORRECTNESS`: Checks grammar and syntax
- `TOXICITY`: Detects harmful or inappropriate content
- `RESPONSE_TONE`: Analyzes the tone of responses
- `ANSWER_RELEVANCE`: Evaluates response relevance
- `FACTUAL_CONSISTENCY`: Checks factual accuracy
- `READABILITY`: Measures text readability
- `CLARITY`: Evaluates clarity of expression

For more metrics and detailed configuration options, refer to the [InspeqAI SDK Documentation](https://docs.inspeq.ai/).

## Response Tracking

All responses are automatically saved in JSON files with timestamps in the format:
```
response_YYYYMMDD_HHMMSS.json
```

Each file contains:
- Timestamp
- Prompt evaluation results
- Claude's response
- Response evaluation results

## Potential improvements
- Add more metrics for prompt evaluation
- Refactor the logging system for better organization
- Add customised exceptions for specific errors
- Human-in-the-loop evaluation mechanism so that users can provide feedback or force a re-evaluation passing on the response from Inspeq AI to Claude and re-generate the content.

## Error Handling

The project includes comprehensive error handling:
- Environment validation
- API error handling
- Response validation through InspeqAI
- Detailed logging
- Faulty responses are flagged and logged
Logs include timestamps and error details for debugging.

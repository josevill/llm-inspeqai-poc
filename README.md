# AI Content Generation and Evaluation Project

This project provides a Python interface to interact with Claude AI for content generation and InspeqAI for content evaluation. It includes a complete workflow for evaluating prompts, generating content, and evaluating responses.

## Features

- Content generation using the latest version of Anthropic's Claude Sonnet 3.5 from their API
- Prompt & Response evaluation using InspeqAI
- Automatic response logging and tracking
- Comprehensive error handling and logging

## Prerequisites

- Python 3.12 or higher, certain libraries may require a more recent version. This PoC was built with Python 3.11.
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

4. Create a `.env` file in the project root:
   ```env
   CLAUDE_API_KEY=your_claude_api_key
   INSPEQ_API_KEY=your_inspeq_api_key
   INSPEQ_PROJECT_ID=your_inspeq_project_id
   ```

## Usage

### Running the Project

```bash
python src/main.py
```

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

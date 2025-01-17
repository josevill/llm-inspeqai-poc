================================================
File: README.md
================================================
# Inspeq Python SDK

- **Website:** [Inspeq.ai](https://www.inspeq.ai)
- **Inspeq App:** [Inspeq App](https://platform.inspeq.ai)
- **Detailed Documentation:** [Inspeq Documentation](https://docs.inspeq.ai)

## Quickstart Guide

### Installation

Install the Inspeq SDK and python-dotenv using pip:

```bash
pip install inspeqai python-dotenv
```

The `python-dotenv` package is recommended for securely managing your environment variables, such as API keys.

### Obtain SDK API Key and Project Key

Get your API key and Project Key from the [Inspeq App](https://platform.inspeq.ai)

### Usage

Here's a basic example of how to use the Inspeq SDK with environment variables:

```python
import os
from dotenv import load_dotenv
from inspeq.client import InspeqEval

# Load environment variables
load_dotenv()

# Initialize the client
INSPEQ_API_KEY = os.getenv("INSPEQ_API_KEY")
INSPEQ_PROJECT_ID = os.getenv("INSPEQ_PROJECT_ID")
INSPEQ_API_URL = os.getenv("INSPEQ_API_URL")  # Required only for our on-prem customers

inspeq_eval = InspeqEval(inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID)

# Prepare input data
input_data = [{
    "prompt": "What is the capital of France?",
    "response": "Paris is the capital of France.",
    "context": "The user is asking about European capitals."
}]

# Define metrics to evaluate
metrics_list = ["RESPONSE_TONE", "FACTUAL_CONSISTENCY", "ANSWER_RELEVANCE"]

try:
    results = inspeq_eval.evaluate_llm_task(
        metrics_list=metrics_list,
        input_data=input_data,
        task_name="capital_question"
    )
    print(results)
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

Make sure to create a `.env` file in your project root with your Inspeq credentials:

```
INSPEQ_API_KEY=your_inspeq_sdk_key
INSPEQ_PROJECT_ID=your_project_id
INSPEQ_API_URL=your_inspeq_backend_url
```

### Available Metrics

```python
metrics_list = [
    "RESPONSE_TONE",
    "ANSWER_RELEVANCE",
    "FACTUAL_CONSISTENCY",
    "CONCEPTUAL_SIMILARITY",
    "READABILITY",
    "COHERENCE",
    "CLARITY",
    "DIVERSITY",
    "CREATIVITY",
    "NARRATIVE_CONTINUITY",
    "GRAMMATICAL_CORRECTNESS",
    "DATA_LEAKAGE",
    "COMPRESSION_SCORE",
    "FUZZY_SCORE",
    "ROUGE_SCORE",
    "BLEU_SCORE",
    "METEOR_SCORE",
    "COSINE_SIMILARITY_SCORE",
    "INSECURE_OUTPUT",
    "INVISIBLE_TEXT",
    "TOXICITY",
    "PROMPT_INJECTION"
]
```

## Features

The Inspeq SDK provides a range of metrics to evaluate language model outputs:

## Response Tone
Assesses the tone and style of the generated response.

## Answer Relevance
Measures the degree to which the generated content directly addresses and pertains to the specific question or prompt provided by the user.

## Factual Consistency
Measures the extent of the model hallucinating i.e. model is making up a response based on its imagination or response is grounded in the context supplied.

## Conceptual Similarity
Measures the extent to which the model response aligns with and reflects the underlying ideas or concepts present in the provided context or prompt.

## Readability
Assesses whether the model response can be read and understood by the intended audience, taking into account factors such as vocabulary complexity, sentence structure, and overall clarity.

## Coherence
Evaluates how well the model generates coherent and logical responses that align with the context of the question.

## Clarity
Assesses the response's clarity in terms of language and structure, based on grammar, readability, concise sentences and words, and less redundancy or diversity.

## Diversity
Assesses the diversity of vocabulary used in a piece of text.

## Creativity
Assesses the ability of the model to generate imaginative, and novel responses that extend beyond standard or expected answers.

## Narrative Continuity
Measures the consistency and logical flow of the response throughout the generated text, ensuring that the progression of events remains coherent and connected.

## Grammatical Correctness
Checks whether the model response adherence to the rules of syntax, is free from errors and follows the conventions of the target language.

## Prompt Injection
Evaluates the susceptibility of language models or AI systems to adversarial prompts that manipulate or alter the system's intended behavior.

## Data Leakage
Measures the extent to which sensitive or unintended information is exposed during model training or inference.

## Insecure Output
Detects whether the response contains insecure or dangerous code patterns that could lead to potential security vulnerabilities.

## Invisible Text
Evaluates if the input contains invisible or non-printable characters that might be used maliciously to hide information or manipulate the model's behavior.

## Toxicity
Evaluates the level of harmful or toxic language present in a given text.

## BLEU Score
Measures the quality of text generated by models by comparing it to one or more reference texts.

## Compression Score
Measures the ratio of the length of the generated summary to the length of the original text.

## Cosine Similarity Score
Measures the similarity between the original text and the generated summary by treating both as vectors in a multi-dimensional space.

## Fuzzy Score
Measures the similarity between two pieces of text based on approximate matching rather than exact matching.

## METEOR Score
Evaluates the quality of generated summaries by comparing them to reference summaries, considering matches at the level of unigrams and accounting for synonyms and stemming.

## ROUGE Score
A set of metrics used to evaluate the quality of generated summaries by comparing them to one or more reference summaries.


## Advanced Usage

### Custom Configurations

You can provide custom configurations for metrics:

```python
metrics_config = {
    "response_tone_config": {
        "threshold": 0.5,
        "custom_labels": ["Negative", "Neutral", "Positive"],
        "label_thresholds": [0, 0.5, 0.7, 1]
    }
}

results = inspeq_eval.evaluate_llm_task(
    metrics_list=["RESPONSE_TONE"],
    input_data=input_data,
    task_name="custom_config_task",
    metrics_config=metrics_config
)
```

## Error Handling

The SDK uses custom exceptions for different types of errors:

- **APIError:** For API related issues
- **ConfigError:** For invalid config related issues
- **InputError:** For invalid input data

## Additional Resources

For detailed API documentation, visit [Inspeq Documentation](https://docs.inspeq.ai).
For support or questions, contact our support team through the Inspeq App.

## License

This SDK is distributed under the terms of the Apache License 2.0.


================================================
File: LICENSE
================================================
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


================================================
File: getting_started.md
================================================
# Getting Started with Inspeq Python SDK

## Overview

The Inspeq Python SDK, `inspeq-py-sdk`, empowers developers with a comprehensive set of tools for evaluating generated text. Whether you're assessing factual consistency, grammatical correctness, or other linguistic aspects, this SDK simplifies the evaluation process. It integrates seamlessly into your Python projects, providing a robust solution for text evaluation.

## Installation

To install the Inspeq Python SDK and the recommended `python-dotenv` package for managing environment variables, use pip:

```bash
pip install inspeqai python-dotenv
```

## Obtaining API Keys

To start using the Inspeq Python SDK, you need API keys. Follow these steps to obtain them:

1. Visit the [Inspeq App](https://platform.inspeq.ai).
2. Sign in or create a new account if you haven't already.
3. Generate your unique API key and Project key from the provided interface.

Remember to keep your API key and Project key secure. They serve as the authentication tokens for accessing the Inspeq APIs from your scripts.

## Integration

The SDK seamlessly integrates into your Python projects, providing a straightforward way to incorporate advanced text evaluation capabilities. Here's a basic example of how to use the SDK:

```python
import os
from dotenv import load_dotenv
from inspeq.client import InspeqEval

# Load environment variables
load_dotenv()

# Initialize the client
INSPEQ_API_KEY = os.getenv("INSPEQ_API_KEY")
INSPEQ_PROJECT_ID = os.getenv("INSPEQ_PROJECT_ID")
INSPEQ_API_URL = os.getenv("INSPEQ_API_URL")  # Required only for on-prem customers

inspeq_eval = InspeqEval(inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID)

# Prepare input data
input_data = [{
    "prompt": "What is the capital of France?",
    "response": "Paris is the capital of France.",
    "context": "The user is asking about European capitals."
}]

# Define metrics to evaluate
metrics_list = ["RESPONSE_TONE", "FACTUAL_CONSISTENCY", "ANSWER_RELEVANCE"]

try:
    results = inspeq_eval.evaluate_llm_task(
        metrics_list=metrics_list,
        input_data=input_data,
        task_name="capital_question"
    )
    print(results)
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

## Environment Variables

Create a `.env` file in your project root with your Inspeq credentials:

```
INSPEQ_API_KEY=your_inspeq_sdk_key
INSPEQ_PROJECT_ID=your_project_id
INSPEQ_API_URL=your_inspeq_backend_url
```

## Next Steps

For more detailed information on available metrics, advanced usage, and best practices, refer to the [full documentation](https://docs.inspeq.ai).

If you encounter any issues or have questions, don't hesitate to reach out to our support team through the Inspeq App.


================================================
File: integration_tests.py
================================================
import os
import pytest
import json
import base64
from dotenv import load_dotenv
from inspeq.client import InspeqEval, APIError

# Load environment variables
load_dotenv()

INSPEQ_API_KEY = os.getenv("INSPEQ_API_KEY")
INSPEQ_PROJECT_ID = os.getenv("INSPEQ_PROJECT_ID")
INSPEQ_API_URL = os.getenv("INSPEQ_API_URL")

def generate_random_task_name(prefix="task", length=8):
    """Generate a random task name with a given prefix and length."""
    import random
    import string
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}_{random_string}"

@pytest.fixture
def random_task_name():
    return generate_random_task_name()

@pytest.fixture
def inspeq_client():
    return InspeqEval(inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID, inspeq_api_url=INSPEQ_API_URL)

def validate_result_structure(result):
    assert "status" in result
    assert "message" in result
    assert "results" in result
    assert isinstance(result["results"], list)

    for item in result["results"]:
        assert "id" in item
        assert "project_id" in item
        assert "task_id" in item
        assert "task_name" in item
        assert "model_name" in item
        assert "source_platform" in item
        assert "data_input_id" in item
        assert "data_input_name" in item
        assert "metric_set_input_id" in item
        assert "metric_set_input_name" in item
        assert "response" in item
        assert "context" in item
        assert "metric_name" in item
        assert "score" in item
        assert "passed" in item
        assert isinstance(item["passed"], bool)
        assert "evaluation_details" in item
        assert "metrics_config" in item
        assert "created_at" in item
        assert "updated_at" in item
        assert "created_by" in item
        assert "updated_by" in item
        assert "is_deleted" in item
        assert "metric_evaluation_status" in item

    assert "user_id" in result
    assert "remaining_credits" in result

def run_test(inspeq_client, metrics_list, input_data, task_name):
    try:
        result = inspeq_client.evaluate_llm_task(
            metrics_list=metrics_list,
            input_data=input_data,
            task_name=task_name
        )
        print(f"Task result: {json.dumps(result, indent=2)}")

        validate_result_structure(result)
        return result

    except APIError as e:
        pytest.fail(f"API Error occurred: {str(e)}")
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {str(e)}")

def test_evaluate_llm_task_generation_metrics(inspeq_client, random_task_name):
    generation_metrics = [
        "RESPONSE_TONE", "ANSWER_RELEVANCE", "FACTUAL_CONSISTENCY", "CONCEPTUAL_SIMILARITY",
        "READABILITY", "COHERENCE", "CLARITY", "DIVERSITY", "CREATIVITY", "NARRATIVE_CONTINUITY",
        "GRAMMATICAL_CORRECTNESS", "PROMPT_INJECTION", "DATA_LEAKAGE", "INSECURE_OUTPUT",
        "INVISIBLE_TEXT", "TOXICITY"
    ]
    input_data = [
        {
            "prompt": "What are the benefits of renewable energy?",
            "response": "Renewable energy sources like solar and wind power offer numerous benefits. They reduce greenhouse gas emissions, decrease dependence on fossil fuels, create jobs in the green energy sector, and can lead to long-term cost savings for consumers and businesses.",
            "context": "The user is researching sustainable energy solutions."
        }
    ]

    run_test(inspeq_client, generation_metrics, input_data, random_task_name)

def test_evaluate_llm_task_summarization_metrics(inspeq_client, random_task_name):
    summarization_metrics = [
        "BLEU_SCORE", "COMPRESSION_SCORE", "COSINE_SIMILARITY_SCORE",
        "FUZZY_SCORE", "METEOR_SCORE", "ROUGE_SCORE"
    ]
    input_data = [
        {
            "context": "Climate change is a global challenge that affects all aspects of our lives. It is caused by the increase in greenhouse gases in the atmosphere, primarily due to human activities such as burning fossil fuels and deforestation. The effects of climate change include rising temperatures, more frequent extreme weather events, sea-level rise, and disruptions to ecosystems. To address this issue, countries around the world are working to reduce their carbon emissions and transition to renewable energy sources.",
            "response": "Climate change, driven by human activities, causes global temperature rise and extreme weather. Countries are working to reduce emissions and adopt renewable energy to combat it.",
            "reference_summary": "Climate change, caused by increased greenhouse gases from human activities, leads to rising temperatures and extreme weather. Global efforts focus on reducing emissions and adopting renewable energy."
        }
    ]

    run_test(inspeq_client, summarization_metrics, input_data, random_task_name)

def test_evaluate_llm_task_special_cases(inspeq_client, random_task_name):
    special_metrics = ["CREATIVITY", "DIVERSITY", "PROMPT_INJECTION", "INSECURE_OUTPUT", "INVISIBLE_TEXT", "TOXICITY"]
    input_data = [
        {
            "prompt": "Write a creative short story about a time-traveling scientist.",
            "response": "Dr. Amelia Chronos adjusted her temporal goggles, heart racing as she prepared to make her first jump through time. The lab hummed with energy as she activated the chrono-field generator. In a flash of blue light, she vanished from 2023 and reappeared in ancient Egypt. To her amazement, she found herself face-to-face with Cleopatra, who mistook her for a goddess from the future. Amelia's scientific curiosity battled with her ethical training as she considered the potential consequences of interacting with such a pivotal historical figure. In the end, she chose to observe silently, gathering invaluable data about the past while safeguarding the timeline. As she returned to her own time, Amelia realized that the true power of time travel lay not in changing history, but in understanding it.",
            "context": "The user is participating in a creative writing contest."
        }
    ]

    run_test(inspeq_client, special_metrics, input_data, random_task_name)


================================================
File: requirements.txt
================================================
certifi==2023.11.17
charset-normalizer==3.3.2
idna==3.6
python-dotenv==1.0.1
requests==2.31.0
urllib3==2.2.0


================================================
File: setup.py
================================================
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="inspeqai",
    version="1.0.29",
    packages=find_packages(include=["inspeq*"]),
    package_data={'inspeq': ['config_file.json']},
    license="Apache 2.0",
    author="Inspeq",
    author_email="support@inspeq.ai",
    install_requires=[
        "requests",
    ],
    description="Inspeq AI Python SDK",
    long_description=long_description,  # Assign the content of your README to long_description
    long_description_content_type="text/markdown",  # Specify the type of content (markdown)
    python_requires=">=3.10",
    project_urls={
        "Documentation": "https://docs.inspeq.ai",
        "Source": "https://github.com/inspeq/inspeq-py-sdk",

    },
)



================================================
File: test_client.py
================================================
import pytest
import json
from unittest.mock import patch, MagicMock
from inspeq.client import InspeqEval, APIError

@pytest.fixture
def inspeq_client():
    return InspeqEval("test_api_key", "test_project_id")

def test_evaluate_llm_task(inspeq_client):
    # Test successful case
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "status": 200,
        "message": "All LLM evaluations successful",
        "data": [
            {
                "metric_name": "RESPONSE_TONE_EVALUATION",
                "score": "0.75",
                "passed": True,
                "evaluation_details": "base64_encoded_details",
                "metrics_config": "base64_encoded_config"
            },
            {
                "metric_name": "FACTUAL_CONSISTENCY_EVALUATION",
                "score": "0.85",
                "passed": True,
                "evaluation_details": "base64_encoded_details",
                "metrics_config": "base64_encoded_config"
            }
        ]
    }

    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        result = inspeq_client.evaluate_llm_task(
            metrics_list=["RESPONSE_TONE", "FACTUAL_CONSISTENCY"],
            input_data=[{
                "prompt": "What is the capital of France?",
                "response": "Paris is the capital of France.",
                "context": "The user is asking about European capitals."
            }],
            task_name="test_task"
        )

        assert result["status"] == 200
        assert result["message"] == "All LLM evaluations successful"
        assert len(result["data"]) == 2

        for item in result["data"]:
            assert "metric_name" in item
            assert "score" in item
            assert "passed" in item
            assert "evaluation_details" in item
            assert "metrics_config" in item
            assert item["metric_name"].replace("_EVALUATION", "") in ["RESPONSE_TONE", "FACTUAL_CONSISTENCY"]

    # Test error case
    mock_response.status_code = 400
    mock_response.text = "Bad Request"

    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        with pytest.raises(APIError, match="API call failed with status code 400: Bad Request"):
            inspeq_client.evaluate_llm_task(
                metrics_list=["RESPONSE_TONE"],
                input_data=[{"response": "test_response"}],
                task_name="test_task"
            )

    # Test with custom metrics configuration
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "status": 200,
        "message": "All LLM evaluations successful",
        "data": [
            {
                "metric_name": "RESPONSE_TONE_EVALUATION",
                "score": "0.6",
                "passed": True,
                "evaluation_details": "base64_encoded_details",
                "metrics_config": "base64_encoded_config"
            }
        ]
    }

    with patch('requests.post') as mock_post:
        mock_post.return_value = mock_response
        result = inspeq_client.evaluate_llm_task(
            metrics_list=["RESPONSE_TONE"],
            input_data=[{
                "prompt": "What is the weather like?",
                "response": "The weather is sunny and warm.",
                "context": "The user is asking about current weather conditions."
            }],
            task_name="test_task",
            metrics_config={
                "response_tone_config": {
                    "threshold": 0.6,
                    "custom_labels": ["Negative", "Neutral", "Positive"],
                    "label_thresholds": [0, 0.3, 0.7, 1]
                }
            }
        )

        assert result["status"] == 200
        assert len(result["data"]) == 1
        assert result["data"][0]["metric_name"] == "RESPONSE_TONE_EVALUATION"
        assert float(result["data"][0]["score"]) >= 0.6


================================================
File: test_config.json
================================================
{
  "global_communication_mode": "async",
  "auto_instrument_mode": 1,
  "evaluations": {
    "LLM": {
      "communication_mode": "sync",
      "auto_instrument_mode": 1,
      "configurations": {
        "answer_relevance_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Irrelevant Answer",
            "Marginally Relevant Answer",
            "Relevant Answer"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "answer_fluency_config": {
          "threshold": 0.5,
          "custom_labels": [
            "PASS",
            "FAIL"
          ],
          "label_thresholds": [
            0,
            0.5,
            1
          ]
        },
        "response_tone_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Negative",
            "Neutral",
            "Positive"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "factual_consistency_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Hallucinated",
            "Inconsistent",
            "Consistent"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "word_count_limit_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Failed",
            "Passed"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "do_not_use_keywords_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Failed",
            "Passed"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "coherence_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Incoherent",
            "Slightly Coherent",
            "Coherent"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "grammatical_correctness_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Incorrect",
            "Partially Correct",
            "Correct"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "conceptual_similarity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Dissimilar",
            "Somewhat similar",
            "Similar"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "readability_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Sophisticated",
            "Moderate",
            "Easy"
          ],
          "label_thresholds": [
            0,
            0.3,
            0.6,
            1
          ]
        },
        "clarity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Clear",
            "Partially Clear",
            "Clear"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.74,
            1
          ]
        },
        "narrative_continuity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Non Continuous",
            "Continuous"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "model_refusal_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "data_leakage_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "creativity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Creative",
            "Creative"
          ],
          "label_thresholds": [
            0,
            0.5,
            1
          ]
        },
        "diversity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Redundant",
            "Non Redundant"
          ],
          "label_thresholds": [
            0,
            0.41,
            1
          ]
        },
        "insecure_output_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "prompt_injection_config": {
          "threshold": 0.61,
          "custom_labels": [
            "Detected",
            "Not Detected"
          ],
          "label_thresholds": [
            0,
            0.61,
            1
          ]
        },
        "compression_score_config": {
          "threshold": 0.8,
          "custom_labels": [
            "Compact Summary",
            "Loose Summary"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "density_score_config": {
          "threshold": 0.2,
          "custom_labels": [
            "Verbose Summarization",
            "Concise Summarization"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "fuzzy_score_config": {
          "threshold": 0.8,
          "custom_labels": [
            "Well Aligned Summarization",
            "Misaligned Summarization"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "rouge_score_config": {
          "threshold": 0.8,
          "custom_labels": [
            "High Overlap",
            "Low Overlap"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "bleu_score_config": {
          "threshold": 0.8,
          "custom_labels": [
            "Highly Conforming",
            "Poorly Conforming"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "meteor_score_config": {
          "threshold": 0.8,
          "custom_labels": [
            "Semantically Accurate",
            "Semantically Drifting"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "bert_score_config": {
          "threshold": 0.8,
          "custom_labels": [
            "Linguistically Congruent",
            "Linguistically Incongruent"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "cosine_similarity_score_config": {
          "threshold": 0.2,
          "custom_labels": [
            "Contextual Synchrony",
            "Contextual Divergence"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "euclidean_distance_score_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Detected",
            "Not Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "toxicity_config":{
          "threshold":0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ]
        },
        "invisible_text_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "get_sentence_embedding_score_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Detected",
            "Not Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        }
      }
    },
    "RAGS": {
      "communication_mode": "sync",
      "auto_instrument_mode": 1,
      "configurations": {
        "retrieval_relevance_config": {
          "threshold": 0.5,
          "custom_labels": [
            "relevant",
            "irrelevant"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "response_coherence_config": {
          "threshold": 0.5,
          "custom_labels": [
            "coherent",
            "incoherent"
          ],
          "label_thresholds": [
            0
          ]
        }
      }
    },
    "SQL": {
      "communication_mode": "async",
      "auto_instrument_mode": 1,
      "configurations": {
        "query_performance_config": {
          "threshold": 0.5,
          "custom_labels": [
            "efficient",
            "inefficient"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "data_security_config": {
          "threshold": 0.5,
          "custom_labels": [
            "secure",
            "insecure"
          ],
          "label_thresholds": [
            0,
            1
          ]
        }
      }
    }
  }
}


================================================
File: usage.md
================================================
# Inspeq Python SDK

- **Website:** [Inspeq.ai](https://www.inspeq.ai)
- **Inspeq App:** [Inspeq App](https://platform.inspeq.ai)
- **Detailed Documentation:** [Inspeq Documentation](https://docs.inspeq.ai)

## Quickstart Guide

### Installation

Install the Inspeq SDK and python-dotenv using pip:

```bash
pip install inspeqai python-dotenv
```

The `python-dotenv` package is recommended for securely managing your environment variables, such as API keys.

### Obtain SDK API Key and Project Key

Get your API key and Project Key from the [Inspeq App](https://platform.inspeq.ai)

### Usage

Here's a basic example of how to use the Inspeq SDK with environment variables:

```python
import os
from dotenv import load_dotenv
from inspeq.client import InspeqEval

# Load environment variables
load_dotenv()

# Initialize the client
INSPEQ_API_KEY = os.getenv("INSPEQ_API_KEY")
INSPEQ_PROJECT_ID = os.getenv("INSPEQ_PROJECT_ID")
INSPEQ_API_URL = os.getenv("INSPEQ_API_URL")  # Required only for our on-prem customers

inspeq_eval = InspeqEval(inspeq_api_key=INSPEQ_API_KEY, inspeq_project_id=INSPEQ_PROJECT_ID)

# Prepare input data
input_data = [{
    "prompt": "What is the capital of France?",
    "response": "Paris is the capital of France.",
    "context": "The user is asking about European capitals."
}]

# Define metrics to evaluate
metrics_list = ["RESPONSE_TONE", "FACTUAL_CONSISTENCY", "ANSWER_RELEVANCE"]

try:
    results = inspeq_eval.evaluate_llm_task(
        metrics_list=metrics_list,
        input_data=input_data,
        task_name="capital_question"
    )
    print(results)
except Exception as e:
    print(f"An error occurred: {str(e)}")
```

Make sure to create a `.env` file in your project root with your Inspeq credentials:

```
INSPEQ_API_KEY=your_inspeq_sdk_key
INSPEQ_PROJECT_ID=your_project_id
INSPEQ_API_URL=your_inspeq_backend_url
```

### Available Metrics

```python
metrics_list = [
    "RESPONSE_TONE",
    "ANSWER_RELEVANCE",
    "FACTUAL_CONSISTENCY",
    "CONCEPTUAL_SIMILARITY",
    "READABILITY",
    "COHERENCE",
    "CLARITY",
    "DIVERSITY",
    "CREATIVITY",
    "NARRATIVE_CONTINUITY",
    "GRAMMATICAL_CORRECTNESS",
    "DATA_LEAKAGE",
    "COMPRESSION_SCORE",
    "FUZZY_SCORE",
    "ROUGE_SCORE",
    "BLEU_SCORE",
    "METEOR_SCORE",
    "COSINE_SIMILARITY_SCORE",
    "INSECURE_OUTPUT",
    "INVISIBLE_TEXT",
    "TOXICITY",
    "PROMPT_INJECTION"
]
```

# Features



The Inspeq SDK provides a range of metrics to evaluate language model outputs:

## Response Tone
Assesses the tone and style of the generated response.

## Answer Relevance
Measures the degree to which the generated content directly addresses and pertains to the specific question or prompt provided by the user.

## Factual Consistency
Measures the extent of the model hallucinating i.e. model is making up a response based on its imagination or response is grounded in the context supplied.

## Conceptual Similarity
Measures the extent to which the model response aligns with and reflects the underlying ideas or concepts present in the provided context or prompt.

## Readability
Assesses whether the model response can be read and understood by the intended audience, taking into account factors such as vocabulary complexity, sentence structure, and overall clarity.

## Coherence
Evaluates how well the model generates coherent and logical responses that align with the context of the question.

## Clarity
Assesses the response's clarity in terms of language and structure, based on grammar, readability, concise sentences and words, and less redundancy or diversity.

## Diversity
Assesses the diversity of vocabulary used in a piece of text.

## Creativity
Assesses the ability of the model to generate imaginative, and novel responses that extend beyond standard or expected answers.

## Narrative Continuity
Measures the consistency and logical flow of the response throughout the generated text, ensuring that the progression of events remains coherent and connected.

## Grammatical Correctness
Checks whether the model response adherence to the rules of syntax, is free from errors and follows the conventions of the target language.

## Prompt Injection
Evaluates the susceptibility of language models or AI systems to adversarial prompts that manipulate or alter the system's intended behavior.

## Data Leakage
Measures the extent to which sensitive or unintended information is exposed during model training or inference.

## Insecure Output
Detects whether the response contains insecure or dangerous code patterns that could lead to potential security vulnerabilities.

## Invisible Text
Evaluates if the input contains invisible or non-printable characters that might be used maliciously to hide information or manipulate the model's behavior.

## Toxicity
Evaluates the level of harmful or toxic language present in a given text.

## BLEU Score
Measures the quality of text generated by models by comparing it to one or more reference texts.

## Compression Score
Measures the ratio of the length of the generated summary to the length of the original text.

## Cosine Similarity Score
Measures the similarity between the original text and the generated summary by treating both as vectors in a multi-dimensional space.

## Fuzzy Score
Measures the similarity between two pieces of text based on approximate matching rather than exact matching.

## METEOR Score
Evaluates the quality of generated summaries by comparing them to reference summaries, considering matches at the level of unigrams and accounting for synonyms and stemming.

## ROUGE Score
A set of metrics used to evaluate the quality of generated summaries by comparing them to one or more reference summaries.


## Advanced Usage

### Custom Configurations

You can provide custom configurations for metrics:

```python
metrics_config = {
    "response_tone_config": {
        "threshold": 0.5,
        "custom_labels": ["Negative", "Neutral", "Positive"],
        "label_thresholds": [0, 0.5, 0.7, 1]
    }
}

results = inspeq_eval.evaluate_llm_task(
    metrics_list=["RESPONSE_TONE"],
    input_data=input_data,
    task_name="custom_config_task",
    metrics_config=metrics_config
)
```

## Error Handling

The SDK uses custom exceptions for different types of errors:

- **APIError:** For API related issues
- **ConfigError:** For invalid config related issues
- **InputError:** For invalid input data

## Additional Resources

For detailed API documentation, visit [Inspeq Documentation](https://docs.inspeq.ai).
For support or questions, contact our support team through the Inspeq App.

## License

This SDK is distributed under the terms of the Apache License 2.0.


================================================
File: .example.env
================================================
INSPEQ_API_KEY=ccscscsxdjdydyyyydyya
INSPEQ_PROJECT_ID=esgcwwda4-1456-686c-01q3-acsfse67e74
INSPEQ_API_URL=https://prod-api.inspeq.ai


================================================
File: inspeq/client.py
================================================
import logging
import requests
import os
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
logger = logging.getLogger(__name__)
class InspeqError(Exception):
    """Base exception class for Inspeq SDK errors."""

class APIError(InspeqError):
    """Exception raised for API-related errors."""

class ConfigError(InspeqError):
    """Exception raised for configuration-related errors."""

class InputError(InspeqError):
    """Exception raised for invalid input errors."""

class InspeqEval:

    DEFAULT_API_URL = "https://prod-api.inspeq.ai"

    def __init__(
        self,
        inspeq_api_key: str,
        inspeq_project_id: str,
        inspeq_api_url: Optional[str] = None,
        log_level: int = logging.INFO
    ):
        if not inspeq_api_key:
            raise ConfigError("No SDK API key provided.")
        if not inspeq_project_id:
            raise ConfigError("No project ID provided.")

        self.inspeq_api_key = inspeq_api_key
        self.inspeq_project_id = inspeq_project_id
        self.inspeq_api_url = inspeq_api_url or os.getenv("INSPEQ_API_URL") or self.DEFAULT_API_URL

        self._setup_logging(log_level)
        self._setup_logging(log_level)

    def _setup_logging(self, log_level: int) -> None:
        logging.basicConfig(level=log_level)
        logger.setLevel(log_level)

    def _handle_http_error(self, response: requests.Response) -> None:
        if response.status_code == 400:
            raise APIError("Bad Request: " + response.text)
        elif response.status_code == 401:
            raise APIError("Unauthorized: SDK API key is not valid.")
        elif response.status_code == 409:
            raise APIError("Conflict: " + response.text)
        elif response.status_code == 422:
            error_detail = response.json().get("detail", "Invalid input.")
            raise InputError(error_detail)
        else:
            raise APIError(f"HTTP Error: {response.status_code} - {response.text}")

    def evaluate_llm_task(
        self,
        metrics_list: List[str],
        input_data: List[Dict[str, str]],
        task_name: Optional[str] = None,
        metrics_config: Optional[Dict] = None
    ) -> Dict:
        url = f"{self.inspeq_api_url}/api/v2/sdk/evaluate_llm"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        request_body = {
            "project_id": self.inspeq_project_id,
            "secret_key": self.inspeq_api_key,
            "metrics": metrics_list,
            "input_data": input_data,
            "task_name": task_name
        }
        payload = {
            "request_body": request_body,
            "metrics_config": metrics_config or {}
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError(f"API call failed with status code {response.status_code}: {response.text}")


================================================
File: inspeq/config_file.json
================================================
{
  "global_communication_mode": "async",
  "auto_instrument_mode": 1,
  "evaluations": {
    "LLM": {
      "communication_mode": "sync",
      "auto_instrument_mode": 1,
      "configurations": {
        "answer_relevance_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Irrelevant Answer",
            "Marginally Relevant Answer",
            "Relevant Answer"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "answer_fluency_config": {
          "threshold": 0.5,
          "custom_labels": [
            "PASS",
            "FAIL"
          ],
          "label_thresholds": [
            0,
            0.5,
            1
          ]
        },
        "response_tone_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Negative",
            "Neutral",
            "Positive"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "factual_consistency_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Hallucinated",
            "Inconsistent",
            "Consistent"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "word_limit_test_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Failed",
            "Passed"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "do_not_use_keywords_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Failed",
            "Passed"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "coherence_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Incoherent",
            "Slightly Coherent",
            "Coherent"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "grammatical_correctness_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Incorrect",
            "Partially Correct",
            "Correct"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "conceptual_similarity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Dissimilar",
            "Somewhat similar",
            "Similar"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        },
        "readability_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Sophisticated",
            "Moderate",
            "Easy"
          ],
          "label_thresholds": [
            0,
            0.3,
            0.6,
            1
          ]
        },
        "clarity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Clear",
            "Partially Clear",
            "Clear"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.74,
            1
          ]
        },
        "narrative_continuity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Non Continuous",
            "Continuous"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "model_refusal_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "insecure_output_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "creativity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Creative",
            "Creative"
          ],
          "label_thresholds": [
            0,
            0.5,
            1
          ]
        },
        "diversity_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Redundant",
            "Non Redundant"
          ],
          "label_thresholds": [
            0,
            0.41,
            1
          ]
        },
        "insecure_output_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Not Detected",
            "Detected"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "prompt_injection_config": {
          "threshold": 0.5,
          "custom_labels": [
            "Low_Confidence",
            "Medium_Confidence",
            "High_Confidence"
          ],
          "label_thresholds": [
            0,
            0.5,
            0.7,
            1
          ]
        }
      }
    },
    "RAGS": {
      "communication_mode": "sync",
      "auto_instrument_mode": 1,
      "configurations": {
        "retrieval_relevance_config": {
          "threshold": 0.5,
          "custom_labels": [
            "relevant",
            "irrelevant"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "response_coherence_config": {
          "threshold": 0.5,
          "custom_labels": [
            "coherent",
            "incoherent"
          ],
          "label_thresholds": [
            0
          ]
        }
      }
    },
    "SQL": {
      "communication_mode": "async",
      "auto_instrument_mode": 1,
      "configurations": {
        "query_performance_config": {
          "threshold": 0.5,
          "custom_labels": [
            "efficient",
            "inefficient"
          ],
          "label_thresholds": [
            0,
            1
          ]
        },
        "data_security_config": {
          "threshold": 0.5,
          "custom_labels": [
            "secure",
            "insecure"
          ],
          "label_thresholds": [
            0,
            1
          ]
        }
      }
    }
  }
}

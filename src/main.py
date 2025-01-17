from ai_client import AIClient
from evaluation_parser import EvaluationParser


def print_evaluation_results(title: str, evaluation_data: dict):
    print(f"\n=== {title} ===")
    if evaluation_data:
        parser = EvaluationParser(evaluation_data)
        print(parser)
    else:
        print("No evaluation data available")


def main():
    client = AIClient()

    prompt = """
Generate a blog post for our reinsurance company.
It needs to be on things related to our profiles and what is to come in the FSI sector for 2025, things like regulations, market trends, market shares or industry standards that are coming into action for the new year.
Leverage the context to tailor the output as closer to the needs of the target audience, keep in mind the Profiles in the context to create the title and paragraphs of the blog post.
Explain any concept in simple terms, if there is the need to use complex jargon of the industry or overall, explain it in a sentence or two.
If you use any acronyms, explain them in a sentence with the full name.
If you use any word that is only used in the industry, make sure to explain it as well.
Keep the technicallity of the output as simple as possible as anyone from within the industry must be able to understand the content, consume it and assimilate it for it to be engaging.
Use the context to build this blog post based on the locations of the profiles, target audiences and their key markets.
Keep in mind the average word count for the output up to the ranges provided by the profiles.
Dont make any assumptions over topics you are not quiet aware or have little to no knowledge about.
Make references to the profiles, target audiences and their key markets, things like 'how Bank X is could tackle Y problem in 2025' for example.
Do not include any odd character or empty characters besides spaces and newlines."""
    context = """We are a reinsurance company, you have the knowledge of the following profiles that consume our content and potentially our services:
Traditional Bank Profile:
Institution: FinoBank AG
Location: Frankfurt, Germany
Type: Traditional Banking Institution
Key Markets: Germany, Austria, Switzerland
Target Audience: Retail investors, Wealth management clients
Regulatory Framework: EU Banking Union, MiFID II
Technical Level: Intermediate
Word Count Range: 1500 words
---
Fintech Company Profile:
Institution: NeoFinance SAS
Location: Paris, France
Type: Digital Financial Services Provider
Key Markets: France, Benelux countries
Target Audience: Tech-savvy investors, Digital natives
Regulatory Framework: EU MiCA, PSD3
Technical Level: Advanced
Word Count Range: 1200~1800 words"""

    prompt_metrics = [
        "DATA_LEAKAGE",
        "INSECURE_OUTPUT",
        "COHERENCE",
        "GRAMMATICAL_CORRECTNESS",
        "TOXICITY",
    ]

    response_metrics = [
        "RESPONSE_TONE",
        "ANSWER_RELEVANCE",
        "FACTUAL_CONSISTENCY",
        "READABILITY",
        "CLARITY",
    ]

    result = client.complete_evaluation_flow(
        prompt=prompt,
        context=context,
        prompt_metrics=prompt_metrics,
        response_metrics=response_metrics,
    )

    # Print all raw results
    print(f"\nClaude Response: {result['response']}")
    print(result["prompt_evaluation"])
    print(result["response_evaluation"])
    print("\n")

    # Formatted results
    print_evaluation_results("Prompt Evaluation", result["prompt_evaluation"])
    print_evaluation_results("Response Evaluation", result["response_evaluation"])


if __name__ == "__main__":
    main()

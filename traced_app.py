from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,
    max_tokens=600,
    timeout=60,
    max_retries=1,
)

prompts = [
    "Explain artificial intelligence in one sentence.",
    "Explain how LangChain and LangSmith differ in about 100 words.",
    (
        "Write a beginner-friendly guide of about 300 words explaining "
        "how an online store can use AI for customer support. "
        "Include three practical examples and two limitations."
    ),
]

for number, prompt in enumerate(prompts, start=1):
    print(f"\n{'=' * 60}")
    print(f"PROMPT {number}: {prompt}")
    print("-" * 60)

    response = llm.invoke(prompt)
    print(response.content)

print("\nAll three prompts completed.")
from llm_service import LLMService, PromptTemplate


template = """
You are a {role}.

Explain {topic} to a {audience}.

Use {style} language.

Provide one real-time example.
"""


prompt_builder = PromptTemplate(template)

llm = LLMService()


# Dynamic input values

prompt = prompt_builder.generate_prompt(

    role="Python Trainer",

    topic="Decorators",

    audience="Beginners",

    style="Simple"
)


print("\nGenerated Prompt:")
print(prompt)


# Send prompt to LLM

response = llm.get_response(prompt)


print("\nAI Response:")
print(response)
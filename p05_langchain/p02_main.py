from p02_prompt_service import PromptService
from p01_llm_service import LLMService


prompt_service = PromptService()
llm_service = LLMService()


topic = input("\nEnter programming topic: ")
level = input("Enter student level: ")
style = input("Enter explanation style: ")
example_required = input("Include code example? (Yes/No): ")


try:

    # Generate formatted messages using dynamic prompt values
    messages = prompt_service.generate_prompt(
        topic=topic,
        level=level,
        style=style,
        example_required=example_required
    )


    print("\nGenerated Prompt Messages:")
    print(messages)

    response = llm_service.get_response(messages)

    print("\nAI Response:")
    print(response)


except Exception as e:
    print("Error:", e)
from p01_llm_service import LLMService

llm = LLMService()


while True:

    user_input = input("\nEnter your question: ")

    if user_input.lower() == "exit":
        print("Thank you for using the AI Assistant!")
        break

    if not user_input.strip():
        print("Please enter a valid question.")
        continue

    try:

        response = llm.get_response(user_input)
        print("\nAI Response:")
        print(response)

    except Exception as e:
        print("Error occurred:", e)
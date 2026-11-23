from p10_agent_service import AgentService


def main():

    print("\n====================================")
    print(" EMPLOYEE AI ASSISTANT")
    print("====================================")

    agent = AgentService()

    while True:
        question = input("\nYou: ")

        if question.lower() == "exit":
            print("\nThank you for using the assistant!")
            break

        if not question.strip():
            print("Please enter a question.")
            continue

        try:
            response = agent.ask_question(question)
            print("\nAI Assistant:", response)

        except Exception as error:
            print("\nError:", error)


if __name__ == "__main__":
    main()
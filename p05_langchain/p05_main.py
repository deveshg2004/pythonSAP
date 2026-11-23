from p05_chain_service import SequentialChainService

def main():

    service = SequentialChainService()

    print("\n===== AI Course Content Generator =====")

    topic = input("\nEnter a topic: ")

    try:

        result = service.generate_course_content(topic)

        print("\n========== TOPIC EXPLANATION ==========")
        print(result["explanation"])

        print("\n========== INTERVIEW QUESTIONS ==========")
        print(result["interview_questions"])

        print("\n========== QUIZ ==========")
        print(result["quiz"])

    except Exception as e:
        print("\nError:", e)


if __name__ == "__main__":
    main()
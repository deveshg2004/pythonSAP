# Import the RAG service.
from p09_rag_service import RAGService


def main():

    print("\n====================================")
    print(" EMPLOYEE HANDBOOK RAG ASSISTANT")
    print("====================================")

    rag = RAGService()

    while True:
        question = input("\nAsk your question (or type exit): ")
       
        if question.lower() == "exit":
            print("\nThank you for using the assistant!")
            break

        if not question.strip():
            print("Please enter a valid question.")
            continue

        try:
            answer, sources = rag.answer_question(question)
            
            print("\n========== ANSWER ==========")
            print(answer)

            print("\n========== SOURCE PAGES ==========")

            for index, document in enumerate(sources, start=1):
                page_number = document.metadata.get("page")

                if page_number is not None:
                    page_number += 1

                print(f"\nSource {index}")
                print("Page:", page_number)
                print("Content:", document.page_content[:300])

        except Exception as error:

            print("\nError:", error)


if __name__ == "__main__":
    main()
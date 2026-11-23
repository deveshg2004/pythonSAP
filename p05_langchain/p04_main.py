from p04_chain_service import ChainService

def main():
    service = ChainService()

    print("\n===== LangChain Output Parser Application =====")
    topic = input("\nEnter the programming topic: ")
    level = input("Enter the explanation level: ")

    try:
        response = service.generate_response(topic, level)

        print("\n===== Generated Response =====")
        print(response)

        print("\n===== Response Data Type =====")
        print(type(response))

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
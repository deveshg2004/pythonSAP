
from p01_graph_service import GraphService


def main():

    user_input = input("\nEnter your text: ")

    graph_service = GraphService()

    result = graph_service.run_graph(user_input)

    print("Cleaned Input :", result["cleaned_input"])

    print("Response      :", result["response"])

    print("\nGraph execution completed successfully.")


if __name__ == "__main__":
    main()

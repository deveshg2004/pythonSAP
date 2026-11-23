import json
from p03_output_service import StructuredOutputService


def main():

    service = StructuredOutputService()

    # Provide unstructured employee information.
    employee_text = """
    Arun Kumar works in the IT department.
    He has four years of professional experience.
    He has worked with Python, SQL, Machine Learning
    and Generative AI technologies.
    """

    print("\nOriginal Employee Information:")
    print(employee_text)

    # Extract structured information using LangChain.
    result = service.extract_employee_profile(employee_text)

    print("\nStructured Output:")
    print(result)

    # Convert the Pydantic object into a Python dictionary.
    employee_data = result.model_dump()

    # Convert the dictionary into formatted JSON.
    json_output = json.dumps(
        employee_data,
        indent=4
    )

    print("\nJSON Output:")
    print(json_output)


if __name__ == "__main__":
    main()
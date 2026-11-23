from langchain_openai import ChatOpenAI
from config import Config
from p03_schemas import EmployeeProfile


class StructuredOutputService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=Config.MODEL,
            temperature=Config.TEMPERATURE,
            api_key=Config.API_KEY
        )

        self.structured_llm = self.llm.with_structured_output(
            EmployeeProfile
        )


    # Extract employee information from unstructured text.
    def extract_employee_profile(self, employee_text):

        # Send the text to the structured LLM.
        # The returned result is a validated Pydantic object.
        response = self.structured_llm.invoke(employee_text)

        return response
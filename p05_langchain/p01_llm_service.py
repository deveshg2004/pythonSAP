# Import ChatOpenAI to connect with OpenAI chat models
from langchain_openai import ChatOpenAI

from config import Config


# Create a class to manage LLM operations
class LLMService:

    def __init__(self):

        # Create a ChatOpenAI model instance
        self.llm = ChatOpenAI(
            model=Config.MODEL,
            temperature=Config.TEMPERATURE,
            api_key=Config.API_KEY
        )


    # Create a method to send a question to the LLM
    def get_response(self, user_input):

        # Send the user input to the model
        # invoke() executes the model request
        response = self.llm.invoke(user_input)

        # Extract the text content from the AIMessage
        return response.content
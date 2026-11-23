from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser

from config import Config
from p04_prompt_service import PromptService


class ChainService:

    # Initialize the chain service.
    def __init__(self):

        # Create the ChatOpenAI model.
        self.llm = ChatOpenAI(
            model=Config.MODEL,
            temperature=Config.TEMPERATURE,
            api_key=Config.API_KEY
        )

        self.prompt_service = PromptService()
        self.output_parser = StrOutputParser()
        self.prompt = self.prompt_service.get_prompt()

        # Connect the prompt, LLM and output parser.
        # The pipe operator creates an LCEL pipeline.
        self.chain = ( self.prompt  | self.llm  | self.output_parser  )


    # Generate a response using the complete chain.
    def generate_response(self, topic, level):

        response = self.chain.invoke({
            "topic": topic,
            "level": level
        })

        return response
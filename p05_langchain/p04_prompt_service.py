# Import ChatPromptTemplate to create reusable prompts.
from langchain_core.prompts import ChatPromptTemplate


class PromptService:

    def __init__(self):

        # Define the system and human messages.
        self.prompt = ChatPromptTemplate.from_messages([

            ("system", """
            You are an experienced Python programming trainer.
            Explain concepts in simple language.
            Use practical examples whenever necessary.
            """),

            ("human", """
            Explain the following topic:

            Topic: {topic}

            Explanation Level: {level}
            """
            )
        ])


    def get_prompt(self):
        return self.prompt
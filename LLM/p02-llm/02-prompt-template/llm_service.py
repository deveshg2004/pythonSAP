from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class PromptTemplate:

    def __init__(self, template):
        self.template = template


    def generate_prompt(self, **kwargs):
        return self.template.format(**kwargs)


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )


    def get_response(self, prompt):

        response = self.client.chat.completions.create(

            model=os.getenv("OPENAI_MODEL"),

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7
        )

        return response.choices[0].message.content
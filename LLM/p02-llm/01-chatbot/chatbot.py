# We maintain the conversation history and send it along with every new request.
# The execution flow:
# 1. User enters a message.
# 2. The message is appended to conversation history.
# 3. Conversation history is sent to the OpenAI API.
# 4. The model generates a response using the previous messages as context.
# 5. The assistant response is appended to conversation history.
# 6. The next user message uses the updated history.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class ChatBot:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.model = os.getenv("OPENAI_MODEL")

        self.temperature = 0.7

        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]


    def get_response(self, user_input):

        # Add user message to history
        self.messages.append({
            "role": "user",
            "content": user_input
        })

        # Send complete conversation history
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature
        )

        # Extract assistant response
        assistant_response = response.choices[0].message.content

        # Add assistant response to history
        self.messages.append({
            "role": "assistant",
            "content": assistant_response
        })

        return assistant_response

    
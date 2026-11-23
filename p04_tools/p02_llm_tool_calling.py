
import json
from openai import OpenAI
from config import Config
from p01_tool_registry import execute_tool

# Define the available tools for OpenAI.

TOOLS = [

    # Calculator Tool Definition

    {
        "type": "function",

        "function": {

            "name": "calculator",

            "description": "Perform mathematical calculations",

            "parameters": {

                "type": "object",

                "properties": {

                    "num1": {
                        "type": "number",
                        "description": "First number"
                    },

                    "num2": {
                        "type": "number",
                        "description": "Second number"
                    },

                    "operation": {
                        "type": "string",
                        "enum": [
                            "add",
                            "subtract",
                            "multiply",
                            "divide"
                        ],
                        "description": "Mathematical operation"
                    }

                },

                "required": [
                    "num1",
                    "num2",
                    "operation"
                ]

            }

        }

    },

    # Date Tool Definition

    {
        "type": "function",

        "function": {

            "name": "date",

            "description": "Get the current date",

            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }

        }

    },

    # Uppercase Tool Definition

    {
        "type": "function",

        "function": {

            "name": "uppercase",

            "description": "Convert the given text into uppercase",

            "parameters": {

                "type": "object",

                "properties": {

                    "text": {
                        "type": "string",
                        "description": "Text to convert"
                    }

                },

                "required": ["text"]

            }

        }

    },

    # Word Count Tool Definition

    {
        "type": "function",

        "function": {

            "name": "word_count",

            "description": "Count the number of words in a sentence",

            "parameters": {

                "type": "object",

                "properties": {

                    "text": {
                        "type": "string",
                        "description": "Sentence to count"
                    }

                },

                "required": ["text"]

            }

        }

    }

]






# Create a class to manage LLM-based tool calling.

class ToolCallingService:

    def __init__(self):

        # Initialize the OpenAI client.

        self.client = OpenAI(
            api_key=Config.API_KEY
        )


    # Method to process the user query.

    def process_query(self, user_query):

        # Prepare the conversation messages.

        messages = [

            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. "
                    "Use the available tools whenever "
                    "they are appropriate for the user's request. "
                    "Do not invent tool results."
                )
            },

            {
                "role": "user",
                "content": user_query
            }

        ]


        # Send the user query and tool definitions
        # to the OpenAI model.

        response = self.client.chat.completions.create(

            model=Config.MODEL,

            messages=messages,

            tools=TOOLS,

            tool_choice="auto",

            parallel_tool_calls=False,

            temperature=Config.TEMPERATURE

        )


        # Retrieve the assistant's response.

        assistant_message = response.choices[0].message


        # Check whether the LLM requested a tool.

        if not assistant_message.tool_calls:

            return assistant_message.content


        # Add the assistant's tool request to conversation history.

        messages.append(assistant_message)


        # Process the selected tool call.

        for tool_call in assistant_message.tool_calls:

            print("\n\n",tool_call,"\n\n")
            
            # Extract the tool name.

            tool_name = tool_call.function.name

            # Extract the tool arguments as JSON.

            arguments = json.loads(
                tool_call.function.arguments
            )


            print("\nSelected Tool:", tool_name)

            print("Tool Arguments:", arguments)


            # Execute the selected Python tool
            # using the centralized registry.

            tool_result = execute_tool(
                tool_name,
                arguments
            )


            print("Tool Result:", tool_result)


            # Send the tool result back to OpenAI.

            messages.append({

                "role": "tool",

                "tool_call_id": tool_call.id,

                "content": json.dumps(
                    tool_result,
                    default=str
                )

            })


        # Ask the LLM to generate the final response
        # using the tool execution result.

        final_response = self.client.chat.completions.create(

            model=Config.MODEL,

            messages=messages,

            temperature=Config.TEMPERATURE

        )


        # Return the final answer.

        return final_response.choices[0].message.content

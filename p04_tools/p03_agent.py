
import json
from openai import OpenAI
from config import Config
from p03_tool_definitions import TOOLS


from p01_tool_registry import execute_tool


class AIAgent:

    # Initialize the AI agent.

    def __init__(self):

        # Create the OpenAI client.

        self.client = OpenAI(
            api_key=Config.API_KEY
        )

        # Set the maximum number of tool-calling rounds.

        self.max_iterations = 10


    # Create a method to process user queries.

    def run(self, user_query):

        # Initialize conversation history.

        messages = [

            {
                "role": "system",
                "content": (
                    "You are an intelligent AI agent. "
                    "Use available tools to complete user tasks. "
                    "For multi-step calculations, use the "
                    "result of one calculation as the input "
                    "for the next calculation. "
                    "After completing the task, provide "
                    "a clear final answer."
                )
            },

            {
                "role": "user",
                "content": user_query
            }

        ]


        # Start the agent execution loop.

        for iteration in range(self.max_iterations):

            print(f"\nAgent Iteration: {iteration + 1}")


            # Send conversation history and available tools
            # to the OpenAI model.

            response = self.client.chat.completions.create(

                model=Config.MODEL,

                messages=messages,

                tools=TOOLS,

                tool_choice="auto",

                parallel_tool_calls=False,

                temperature=Config.TEMPERATURE

            )


            # Extract the assistant message.

            assistant_message = response.choices[0].message


            # Check whether the LLM requested a tool.

            if not assistant_message.tool_calls:

                print("\nAgent completed the task.")

                return assistant_message.content


            # Add the assistant's tool request
            # to conversation history.

            messages.append(assistant_message)


            # Process every requested tool call.

            for tool_call in assistant_message.tool_calls:

                # Extract the tool name.

                tool_name = tool_call.function.name


                # Extract tool arguments from JSON.

                arguments = json.loads(
                    tool_call.function.arguments
                )


                print("\nSelected Tool:", tool_name)

                print("Arguments:", arguments)


                # Execute the selected Python tool.

                result = execute_tool(
                    tool_name,
                    arguments
                )


                print("Tool Result:", result)


                # Add the tool result to conversation history.

                messages.append({

                    "role": "tool",

                    "tool_call_id": tool_call.id,

                    "content": json.dumps(
                        result,
                        default=str
                    )

                })


        # Stop execution if maximum iterations are reached.

        return (
            "Agent stopped: Maximum execution "
            "iterations reached."
        )

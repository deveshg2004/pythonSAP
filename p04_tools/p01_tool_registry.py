
# Import all the tools from tools.py

from p01_tools import (
    calculator_tool,
    date_tool,
    text_uppercase_tool,
    word_count_tool
)


# Create a centralized tool registry.
# Dictionary keys represent tool names.
# Dictionary values represent Python functions.

TOOL_REGISTRY = {

    "calculator": calculator_tool,

    "date": date_tool,

    "uppercase": text_uppercase_tool,

    "word_count": word_count_tool

}


# Function to retrieve and execute a tool
# based on the tool name.

def execute_tool(tool_name: str, arguments: dict):

    # Check whether the requested tool exists.

    if tool_name not in TOOL_REGISTRY:

        return "Error: Tool not found"

    # Retrieve the corresponding Python function.

    selected_tool = TOOL_REGISTRY[tool_name]

    # Execute the selected function
    # by passing the supplied arguments.

    result = selected_tool(**arguments)

    return result

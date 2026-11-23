
# Import the execute_tool function
# from the centralized tool registry.

from p01_tool_registry import execute_tool


# Execute Calculator Tool

result = execute_tool(
    "calculator",
    {
        "num1": 100,
        "num2": 50,
        "operation": "add"
    }
)

print("Calculator Result:", result)


# Execute Date Tool

result = execute_tool(
    "date",
    {}
)

print("Current Date:", result)


# Execute Uppercase Tool

result = execute_tool(
    "uppercase",
    {
        "text": "Welcome to Generative AI"
    }
)

print("Uppercase Result:", result)


# Execute Word Count Tool

result = execute_tool(
    "word_count",
    {
        "text": "Python AI Generative AI Training"
    }
)

print("Word Count:", result)


# Execute an unknown tool

result = execute_tool(
    "weather",
    {}
)

print("Unknown Tool Result:", result)

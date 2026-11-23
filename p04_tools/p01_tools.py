
from datetime import datetime


# Tool 1: Calculator Tool
# This function accepts two numbers and an operation.
# It performs the requested mathematical calculation.

def calculator_tool(num1: float, num2: float, operation: str):

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":

        if num2 == 0:
            return "Error: Division by zero is not allowed"

        return num1 / num2

    else:
        return "Error: Invalid operation"


# Tool 2: Date Tool
# This function retrieves the current date
# and returns it in a readable format.

def date_tool():

    current_date = datetime.now()

    return current_date.strftime("%d-%m-%Y")


# Tool 3: Text Tool
# This function converts the given text into uppercase.

def text_uppercase_tool(text: str):

    return text.upper()


# Tool 4: Word Count Tool
# This function counts the number of words
# present in the given sentence.

def word_count_tool(text: str):

    words = text.split()

    return len(words)


# Define the tools available to the LLM.

TOOLS = [

    # Calculator Tool

    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform mathematical calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "num1": {
                        "type": "number"
                    },
                    "num2": {
                        "type": "number"
                    },
                    "operation": {
                        "type": "string",
                        "enum": [
                            "add",
                            "subtract",
                            "multiply",
                            "divide"
                        ]
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

    # Date Tool

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

    # Uppercase Tool

    {
        "type": "function",
        "function": {
            "name": "uppercase",
            "description": "Convert text into uppercase",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    }
                },
                "required": ["text"]
            }
        }
    },

    # Word Count Tool

    {
        "type": "function",
        "function": {
            "name": "word_count",
            "description": "Count the words in a sentence",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    }
                },
                "required": ["text"]
            }
        }
    }

]

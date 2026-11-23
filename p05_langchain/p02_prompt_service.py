from langchain_core.prompts import ChatPromptTemplate


class PromptService:

    def __init__(self):
        self.prompt = ChatPromptTemplate.from_messages([

            # Define the system instruction
            (
                "system",
                """
                You are an experienced Python trainer.

                Explain programming concepts clearly.

                Adapt your explanation to the student's level.

                Use practical examples whenever required.
                """
            ),

            # Define the user message with dynamic placeholders
            (
                "human",
                """
                Explain the following programming topic.

                Topic: {topic}

                Student Level: {level}

                Explanation Style: {style}

                Include Code Example: {example_required}
                """
            )

        ])


    # Create a method to generate formatted messages
    def generate_prompt(self, topic, level, style, example_required):

        # Pass dynamic values into the prompt template
        formatted_messages = self.prompt.format_messages(
            topic=topic,
            level=level,
            style=style,
            example_required=example_required
        )

        return formatted_messages
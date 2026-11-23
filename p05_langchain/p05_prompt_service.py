from langchain_core.prompts import ChatPromptTemplate


class PromptService:

    def __init__(self):

        # Prompt for generating a topic explanation.
        self.explanation_prompt = ChatPromptTemplate.from_template(
            """
            You are an experienced Python trainer.

            Explain the following topic in simple language
            suitable for beginners.

            Topic: {topic}

            Include:
            1. Definition
            2. Important concepts
            3. Practical example
            4. Real-world application
            """
        )

        # Prompt for generating interview questions.
        self.interview_prompt = ChatPromptTemplate.from_template(
            """
            You are a technical interviewer.

            Based on the following explanation, generate
            five beginner-level interview questions.

            Topic: {topic}

            Explanation:
            {explanation}

            Provide only the questions in a numbered list.
            """
        )

        # Prompt for generating a quiz.
        self.quiz_prompt = ChatPromptTemplate.from_template(
            """
            You are an assessment creator.

            Based on the following explanation, create
            three multiple-choice questions.

            Topic: {topic}

            Explanation:
            {explanation}

            For each question:
            1. Provide four options.
            2. Identify the correct answer.
            3. Give a short explanation.

            Keep the questions suitable for beginners.
            """
        )
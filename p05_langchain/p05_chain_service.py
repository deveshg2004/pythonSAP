from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from config import Config

from p05_prompt_service import PromptService


class SequentialChainService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=Config.MODEL,
            temperature=Config.TEMPERATURE,
            api_key=Config.API_KEY
        )

        self.prompt_service = PromptService()
        self.parser = StrOutputParser()

        # Create the first chain for topic explanation.
        self.explanation_chain = (
            self.prompt_service.explanation_prompt
            | self.llm
            | self.parser
        )

        # Create the second chain for interview questions.
        self.interview_chain = (
            self.prompt_service.interview_prompt
            | self.llm
            | self.parser
        )

        # Create the third chain for quiz generation.
        self.quiz_chain = (
            self.prompt_service.quiz_prompt
            | self.llm
            | self.parser
        )


    def generate_course_content(self, topic):

        explanation = self.explanation_chain.invoke({
            "topic": topic
        })

        interview_questions = self.interview_chain.invoke({
            "topic": topic,
            "explanation": explanation
        })

        quiz = self.quiz_chain.invoke({
            "topic": topic,
            "explanation": explanation
        })

        # Return all three generated results.
        return {
            "explanation": explanation,
            "interview_questions": interview_questions,
            "quiz": quiz
        }
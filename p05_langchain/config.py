import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL = os.getenv("OPENAI_MODEL")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
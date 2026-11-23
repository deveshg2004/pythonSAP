import os

from dotenv import load_dotenv
load_dotenv()

class Config:
    API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "text-embedding-3-small"
    )
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
    DOCUMENT_FOLDER = "documents"
    PDF_PATH = os.path.join(
        DOCUMENT_FOLDER,
        "employee_handbook.pdf"
    )
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100
    TOP_K = 3
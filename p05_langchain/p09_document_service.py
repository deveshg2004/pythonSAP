from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from p09_config import Config


class DocumentService:

    def __init__(self):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )


    def load_and_split(self):
        loader = PyPDFLoader(Config.PDF_PATH)
        pages = loader.load()
        chunks = self.text_splitter.split_documents(pages)
        return pages, chunks
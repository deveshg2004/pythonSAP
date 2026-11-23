# Import ChatOpenAI to communicate with the chat model.
from langchain_openai import ChatOpenAI

# Import OpenAIEmbeddings to convert text into numerical vectors.
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from p09_config import Config
from p09_document_service import DocumentService


class RAGService:

    def __init__(self):

        if not Config.API_KEY:
            raise ValueError("OPENAI_API_KEY is missing in .env")

        self.document_service = DocumentService()

        # Create the embedding model.
        self.embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            api_key=Config.API_KEY
        )

        # Create the chat model.
        self.llm = ChatOpenAI(
            model=Config.MODEL,
            temperature=Config.TEMPERATURE,
            api_key=Config.API_KEY
        )

        # Build the vector database and retriever.
        self.create_vector_store()

        # Create the RAG prompt and chain.
        self.create_rag_chain()


    # Define a method to create the FAISS vector database.
    def create_vector_store(self):
        pages, chunks = self.document_service.load_and_split()
        print("\nTotal Pages Loaded:", len(pages))
        print("Total Chunks Generated:", len(chunks))

        self.vector_store = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": Config.TOP_K}
        )

        print("FAISS Vector Database Created Successfully!")


    # Define a method to create the RAG prompt and chain.
    def create_rag_chain(self):

        # Create a prompt that instructs the LLM to use retrieved context.
        self.prompt = ChatPromptTemplate.from_template(
            """
            You are an employee handbook assistant.

            Answer the user's question using only the
            information provided in the context.

            If the answer is not available in the context,
            clearly say that the information is not available
            in the employee handbook.

            Do not invent policies or information.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """
        )

        # Connect the prompt, LLM and output parser.
        self.rag_chain = (
            self.prompt
            | self.llm
            | StrOutputParser()
        )


    def answer_question(self, question):
        retrieved_docs = self.retriever.invoke(question)

        # Combine the retrieved chunk content into one context string.
        context = "\n\n".join(
            document.page_content
            for document in retrieved_docs
        )

        # Pass the retrieved context and question to the RAG chain.
        answer = self.rag_chain.invoke({
            "context": context,
            "question": question
        })

        # Return the answer and retrieved source documents.
        return answer, retrieved_docs
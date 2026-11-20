
# Import json to save embeddings in a JSON file.
import json

# Import the PDF document loader.
from p01_document_loader import DocumentLoader

# Import the text processor.
from p02_text_processor import TextProcessor

# Import the text splitter.
from p03_text_splitter import TextSplitter

# Import the embedding generator.
from p04_embedding_generator import EmbeddingGenerator


# Specify the PDF document location.
file_path = "documents/employee_handbook.pdf"


try:

    # Step 1: Load the PDF document.
    loader = DocumentLoader(file_path)

    # Extract text from all PDF pages.
    documents = loader.load_document()

    # Stop if no PDF content was extracted.
    if not documents:
        raise ValueError("No content was extracted from the PDF")

    # Step 2: Clean the extracted text.
    processor = TextProcessor()

    # Process the page-wise documents.
    processed_documents = processor.process_documents(documents)

    # Step 3: Split the cleaned text into chunks.
    splitter = TextSplitter()

    # Generate chunks while preserving metadata.
    chunks = splitter.split_documents(
        processed_documents,
        file_path
    )

    # Stop if no chunks were generated.
    if not chunks:
        raise ValueError("No chunks were generated")

    # Display the number of chunks.
    print("\nTotal Chunks:", len(chunks))

    # Step 4: Generate embeddings for the chunks.
    generator = EmbeddingGenerator()

    # Convert all chunks into numerical vectors.
    embedded_chunks, total_tokens = generator.generate_embeddings(chunks)

    # Step 5: Save the embedded chunks into a JSON file.
    with open("embeddings.json", "w", encoding="utf-8") as file:

        # Convert Python objects into JSON format.
        json.dump(
            embedded_chunks,
            file,
            indent=4,
            ensure_ascii=False
        )

    # Display the total number of embedded chunks.
    print("\nTotal Embedded Chunks:", len(embedded_chunks))

    # Display the total number of API input tokens used.
    print("Total Tokens Used:", total_tokens)

    # Display the embedding dimension of the first chunk.
    print(
        "Embedding Dimensions:",
        len(embedded_chunks[0]["embedding"])
    )

    # Display details of the first embedded chunk.
    print("\nFirst Chunk ID:", embedded_chunks[0]["chunk_id"])

    # Display only the first five vector values.
    print(
        "First Five Values:",
        embedded_chunks[0]["embedding"][:5]
    )

    # Confirm that the embeddings were saved.
    print("\nEmbeddings saved successfully in embeddings.json")


except Exception as error:

    # Display an understandable error message.
    print("\nError:", error)

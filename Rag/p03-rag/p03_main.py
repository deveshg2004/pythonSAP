
# Import the PDF document loader.
from p01_document_loader import DocumentLoader

# Import the text processor.
from p02_text_processor import TextProcessor

# Import the text splitter.
from p03_text_splitter import TextSplitter


# Specify the location of the employee handbook PDF.
file_path = "documents/employee_handbook.pdf"


# Create an object of the DocumentLoader class.
loader = DocumentLoader(file_path)

# Load text from all PDF pages.
documents = loader.load_document()


# Create an object of the TextProcessor class.
processor = TextProcessor()

# Clean the extracted text.
processed_documents = processor.process_documents(documents)


# Create an object of the TextSplitter class.
splitter = TextSplitter()

# Divide the cleaned documents into chunks.
chunks = splitter.split_documents(
    processed_documents,
    file_path
)


# Display the total number of generated chunks.
print("\nTotal Chunks Generated:", len(chunks))


# Display each chunk and its metadata.
for chunk in chunks:

    # Print a separator between chunks.
    print("\n" + "=" * 60)

    # Display the unique chunk identifier.
    print("Chunk ID:", chunk["chunk_id"])

    # Display the original PDF page number.
    print("Page Number:", chunk["page_number"])

    # Display the chunk sequence number.
    print("Chunk Number:", chunk["chunk_number"])

    # Display the number of characters.
    print("Character Count:", chunk["character_count"])

    # Display the actual chunk content.
    print("\nContent:")
    print(chunk["content"])

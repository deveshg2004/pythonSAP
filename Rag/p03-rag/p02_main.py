# Import the DocumentLoader class
from p01_document_loader import DocumentLoader

# Import the TextProcessor class
from p02_text_processor import TextProcessor


# Specify the PDF document location
file_path = "documents/employee_handbook.pdf"


# Create an object of DocumentLoader
loader = DocumentLoader(file_path)


# Extract text from the PDF
documents = loader.load_document()


# Create an object of TextProcessor
processor = TextProcessor()


# Clean and process the extracted documents
processed_documents = processor.process_documents(documents)


# Display the processed information
for document in processed_documents:

    # Print a separator
    print("\n--------------------------------")

    # Display the page number
    print("Page Number:", document["page_number"])

    # Display the character count
    print("Character Count:", document["character_count"])

    # Print the cleaned content
    print("\nCleaned Content:")

    print(document["content"])


# Display the total number of processed pages
print("\nTotal Processed Pages:", len(processed_documents))
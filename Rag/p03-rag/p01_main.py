# Import the DocumentLoader class from document_loader.py
from p01_document_loader import DocumentLoader


# Specify the location of the PDF document
file_path = "documents/employee_handbook.pdf"


# Create an object of the DocumentLoader class
loader = DocumentLoader(file_path)


# Call the load_document() method to extract PDF content
documents = loader.load_document()


# Iterate through the extracted pages
for document in documents:

    # Print a separator for better readability
    print("\n--------------------------------")

    # Display the page number
    print("Page Number:", document["page_number"])

    # Print another separator
    print("--------------------------------")

    # Display the extracted text from the current page
    print(document["content"])
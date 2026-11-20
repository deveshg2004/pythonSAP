# Import PdfReader from the pypdf library to read PDF documents
from pypdf import PdfReader


# Create a class to handle PDF document loading operations
class DocumentLoader:

    # Initialize the class with the PDF file path
    def __init__(self, file_path):

        # Store the PDF file path for future use
        self.file_path = file_path


    # Define a method to load and extract content from the PDF
    def load_document(self):

        try:

            # Open the PDF file using PdfReader
            reader = PdfReader(self.file_path)

            # Get the total number of pages in the PDF
            total_pages = len(reader.pages)

            # Display the total number of pages
            print("Total Pages:", total_pages)

            # Create an empty list to store extracted page information
            documents = []

            # Iterate through every page in the PDF
            # enumerate() provides both the page number and page object
            # start=1 makes page numbering begin from 1 instead of 0
            for page_number, page in enumerate(reader.pages, start=1):

                # Extract text from the current page
                # If no extractable text exists, use an empty string
                text = page.extract_text() or ""

                # Create a dictionary to store page content and metadata
                document = {

                    # Store the current page number
                    "page_number": page_number,

                    # Store the extracted text
                    "content": text
                }

                # Add the current page information to the documents list
                documents.append(document)

            # Return all extracted pages to the calling program
            return documents

        # Handle errors that may occur while reading the PDF
        except Exception as e:

            # Display the error message
            print("Error loading PDF:", e)

            # Return an empty list if document loading fails
            return []
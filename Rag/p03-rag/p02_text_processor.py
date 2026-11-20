# Import the regular expression module
import re


# Create a class to process extracted PDF text
class TextProcessor:

    # Define a method to clean text
    def clean_text(self, text):

        # Remove leading and trailing spaces
        text = text.strip()

        # Replace multiple spaces or tabs with a single space
        text = re.sub(r"[ \t]+", " ", text)

        # Replace three or more consecutive newlines with two newlines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Return the cleaned text
        return text


    # Define a method to process all extracted pages
    def process_documents(self, documents):

        # Create an empty list to store processed pages
        processed_documents = []

        # Iterate through each extracted page
        for document in documents:

            # Get the extracted content
            text = document["content"]

            # Clean the extracted content
            cleaned_text = self.clean_text(text)

            # Check whether the page contains meaningful content
            if cleaned_text.strip():

                # Create a new dictionary with cleaned content
                processed_document = {

                    # Preserve the original page number
                    "page_number": document["page_number"],

                    # Store the cleaned content
                    "content": cleaned_text,

                    # Calculate the character count
                    "character_count": len(cleaned_text)
                }

                # Add the processed page to the list
                processed_documents.append(processed_document)

        # Return all processed pages
        return processed_documents
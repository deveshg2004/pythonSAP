
class TextSplitter:

    # This method splits one large text into smaller chunks.
    def split_text(self, text, chunk_size=500, chunk_overlap=100):

        # Validate the chunk size.
        if chunk_size <= 0:
            raise ValueError("Chunk size must be greater than zero")

        # Overlap cannot be negative or equal to the chunk size.
        if chunk_overlap < 0 or chunk_overlap >= chunk_size:
            raise ValueError("Overlap must be between zero and chunk size")

        # This list stores all the generated chunks.
        chunks = []

        # Start reading the text from the beginning.
        start = 0

        # Continue until the entire text has been processed.
        while start < len(text):

            # Calculate the ending position of the current chunk.
            end = min(start + chunk_size, len(text))

            # Extract a portion of the original text.
            chunk = text[start:end].strip()

            # Avoid adding empty chunks.
            if chunk:
                chunks.append(chunk)

            # Stop when the end of the text has been reached.
            if end == len(text):
                break

            # Move forward while retaining the required overlap.
            start = end - chunk_overlap

        # Return all the generated chunks.
        return chunks

    # This method splits multiple page-wise documents.
    def split_documents(self, documents, source):

        # This list stores the final chunks with their metadata.
        all_chunks = []

        # Process each page separately.
        for document in documents:

            # Read the page number.
            page_number = document["page_number"]

            # Read the cleaned text of the current page.
            text = document["content"]

            # Split the page text into smaller chunks.
            page_chunks = self.split_text(text)

            # Process each generated chunk.
            for index, chunk_text in enumerate(page_chunks, start=1):

                # Store the chunk along with its metadata.
                chunk_data = {
                    "chunk_id": f"page_{page_number}_chunk_{index}",
                    "page_number": page_number,
                    "chunk_number": index,
                    "source": source,
                    "content": chunk_text,
                    "character_count": len(chunk_text)
                }

                # Add the chunk to the final list.
                all_chunks.append(chunk_data)

        # Return all chunks from all pages.
        return all_chunks

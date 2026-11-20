
# Import os to read environment variables.
import os

# Import the OpenAI Python client.
from openai import OpenAI

# Import load_dotenv to load values from the .env file.
from dotenv import load_dotenv


class EmbeddingGenerator:

    # Initialize the embedding generator.
    def __init__(self):

        # Load environment variables from the .env file.
        load_dotenv()

        # Read the OpenAI API key from the environment.
        api_key = os.getenv("OPENAI_API_KEY")

        # Stop execution if the API key is missing.
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing in the .env file")

        # Read the embedding model name from the environment.
        self.model = os.getenv(
            "OPENAI_EMBEDDING_MODEL",
            "text-embedding-3-small"
        )

        # Create the OpenAI client using the API key.
        self.client = OpenAI(api_key=api_key)

    # Generate embeddings for a collection of chunks.
    def generate_embeddings(self, chunks, batch_size=100):

        # Store all chunks along with their generated embeddings.
        embedded_chunks = []

        # Store the total number of tokens used by the API.
        total_tokens = 0

        # Process the chunks in smaller batches.
        for start in range(0, len(chunks), batch_size):

            # Select the current batch of chunks.
            batch = chunks[start:start + batch_size]

            # Extract only the text content from each chunk.
            batch_texts = [
                chunk["content"]
                for chunk in batch
            ]

            # Send multiple text inputs in one API request.
            response = self.client.embeddings.create(
                model=self.model,
                input=batch_texts
            )

            # Read the token usage for the current API request.
            total_tokens += response.usage.total_tokens

            # Process each embedding returned by the API.
            for result in response.data:

                # Use the response index to find the matching chunk.
                original_chunk = batch[result.index]

                # Copy the original chunk and its metadata.
                chunk_with_embedding = original_chunk.copy()

                # Attach the numerical embedding vector.
                chunk_with_embedding["embedding"] = result.embedding

                # Store the completed chunk.
                embedded_chunks.append(chunk_with_embedding)

        # Return the embedded chunks and total token usage.
        return embedded_chunks, total_tokens


    #######################################################
    # For Next Program
    ######################################################
    # Generate an embedding for a single user question.
    def generate_query_embedding(self, question):

        # Send the question to the embedding model.
        response = self.client.embeddings.create(
            model=self.model,
            input=question
        )

        # Extract and return the question embedding.
        return response.data[0].embedding

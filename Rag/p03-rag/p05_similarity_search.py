
# Import the math module for calculating square roots.
import math


class SimilaritySearch:

    # Calculate cosine similarity between two vectors.
    def cosine_similarity(self, vector_a, vector_b):

        # Ensure that both vectors have the same dimensions.
        if len(vector_a) != len(vector_b):
            raise ValueError("Both vectors must have the same dimensions")

        # Calculate the dot product of the two vectors.
        dot_product = sum(
            a * b
            for a, b in zip(vector_a, vector_b)
        )

        # Calculate the magnitude of the first vector.
        magnitude_a = math.sqrt(
            sum(a * a for a in vector_a)
        )

        # Calculate the magnitude of the second vector.
        magnitude_b = math.sqrt(
            sum(b * b for b in vector_b)
        )

        # Prevent division by zero.
        if magnitude_a == 0 or magnitude_b == 0:
            raise ValueError("Cosine similarity is undefined for a zero vector")

        # Apply the cosine similarity formula.
        similarity = dot_product / (magnitude_a * magnitude_b)

        # Return the calculated similarity score.
        return similarity

    # Compare a query embedding with all stored document embeddings.
    def search(self, query_embedding, embedded_chunks, top_k=3):

        # Store each chunk along with its similarity score.
        results = []

        # Compare the question against every document chunk.
        for chunk in embedded_chunks:

            # Read the embedding stored for the current chunk.
            document_embedding = chunk["embedding"]

            # Calculate the similarity score.
            score = self.cosine_similarity(
                query_embedding,
                document_embedding
            )

            # Store the original chunk and its similarity score.
            result = {
                "chunk_id": chunk["chunk_id"],
                "page_number": chunk["page_number"],
                "content": chunk["content"],
                "similarity_score": score
            }

            # Add the result to the collection.
            results.append(result)

        # Sort results from highest similarity to lowest.
        results.sort(
            key=lambda item: item["similarity_score"],
            reverse=True
        )

        # Return only the requested number of top results.
        return results[:top_k]


# Import json to read the previously stored embeddings.
import json

# Import the embedding generator.
from p04_embedding_generator import EmbeddingGenerator

# Import the similarity search class.
from p05_similarity_search import SimilaritySearch


try:

    # Step 1: Read the stored document embeddings.
    with open("embeddings.json", "r", encoding="utf-8") as file:

        # Convert the JSON data into Python objects.
        embedded_chunks = json.load(file)

    # Stop if the JSON file contains no chunks.
    if not embedded_chunks:
        raise ValueError("No embedded chunks found")

    # Step 2: Get a question from the user.
    question = input("\nEnter your question: ").strip()

    # Stop if the user enters an empty question.
    if not question:
        raise ValueError("Please enter a valid question")

    # Step 3: Create an embedding generator object.
    generator = EmbeddingGenerator()

    # Convert the user question into an embedding.
    query_embedding = generator.generate_query_embedding(question)

    # Step 4: Create a similarity search object.
    search_engine = SimilaritySearch()

    # Compare the query with all document embeddings.
    search_results = search_engine.search(
        query_embedding,
        embedded_chunks,
        top_k=3
    )

    # Step 5: Display the retrieved results.
    print("\nTop Matching Results")

    # Process each matching chunk.
    for index, result in enumerate(search_results, start=1):

        # Display the result number.
        print("\n" + "=" * 60)
        print("Result:", index)

        # Display the original document page number.
        print("Page Number:", result["page_number"])

        # Display the unique chunk identifier.
        print("Chunk ID:", result["chunk_id"])

        # Display the similarity score.
        print(
            "Similarity Score:",
            round(result["similarity_score"], 4)
        )

        # Display the retrieved text.
        print("\nContent:")
        print(result["content"])


except Exception as error:

    # Display an understandable error message.
    print("\nError:", error)

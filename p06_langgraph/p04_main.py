from p06_langgraph.p04_graph_service import ContentReviewGraph

content_system = ContentReviewGraph()
topic = input("Enter a topic for content generation: ")
result = content_system.run(topic)

print("\n========== FINAL CONTENT ==========")
print(result["content"])

print("\nReview Attempts:", result["review_attempts"])
print("Review Status:", result["review_status"])
print("Review Feedback:", result["review_feedback"])

print("Final Status:", result["final_status"] if "final_status" in result else result["review_status"])
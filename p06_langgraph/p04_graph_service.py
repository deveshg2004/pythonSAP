from langgraph.graph import StateGraph, START, END
from p06_langgraph.p04_state import ContentState


class ContentReviewGraph:

    def __init__(self):

        # Set the maximum number of review attempts.
        self.max_attempts = 3

        # Create the StateGraph using ContentState.
        self.graph = StateGraph(ContentState)

        # Register the nodes.
        self.graph.add_node("generate_content", self.generate_content)
        self.graph.add_node("review_content", self.review_content)
        self.graph.add_node("improve_content", self.improve_content)

        self.graph.add_edge(START, "generate_content")
        self.graph.add_edge("generate_content", "review_content")
        self.graph.add_conditional_edges( "review_content",
            self.route_after_review,
            {
                "approved": END,
                "improve": "improve_content",
                "max_attempts": END
            }
        )

        self.graph.add_edge("improve_content", "review_content")

        self.app = self.graph.compile()


    # Node 1: Generate the initial content.
    def generate_content(self, state: ContentState):

        topic = state["topic"]

        content = (
            f"{topic}\n\n"
            f"{topic} is an important subject. "
            f"It is useful to understand its basic concepts."
        )

        return {
            "content": content,
            "review_attempts": 0,
            "review_status": "Pending",
            "review_feedback": "Content is waiting for review."
        }


    # Node 2: Review the generated content.
    def review_content(self, state: ContentState):

        content = state["content"]
        attempts = state.get("review_attempts", 0) + 1
        required_sections = [
            "Introduction",
            "Benefits",
            "Conclusion"
        ]

        missing_sections = [
            section
            for section in required_sections
            if section.lower() not in content.lower()
        ]

        # Count the words in the current content.
        word_count = len(content.split())

        # Check whether all mandatory sections are available
        # and whether the content has at least 60 words.
        if not missing_sections and word_count >= 60:
            review_status = "Approved"
            feedback = "All mandatory sections are present and content meets the word-count requirement."

        else:

            review_status = "Needs Improvement"

            feedback = (
                f"Missing sections: {missing_sections}. "
                f"Current word count: {word_count}. "
                f"Required word count: 60."
            )

        return {
            "review_attempts": attempts,
            "review_status": review_status,
            "review_feedback": feedback
        }


    # Routing function: Decide what happens after the review.
    def route_after_review(self, state: ContentState):

        if state["review_status"] == "Approved":
            return "approved"

        if state["review_attempts"] >= self.max_attempts:
            return "max_attempts"

        # Otherwise, send the content for improvement.
        return "improve"


    # Node 3: Improve the content based on the review attempt.
    def improve_content(self, state: ContentState):

        content = state["content"]
        attempts = state["review_attempts"]

        # Add the Benefits section during the first improvement.
        if attempts == 1:
            content += (
                "\n\nBenefits\n"
                "Understanding this topic provides several benefits. "
                "It improves knowledge, supports better decision-making, "
                "and helps people apply concepts in practical situations."
            )

        # Add the Conclusion section during the second improvement.
        elif attempts == 2:

            # Append the conclusion.
            content += (
                "\n\nConclusion\n"
                "In conclusion, learning this subject helps build a strong "
                "foundation. Regular practice and practical application "
                "can improve understanding and confidence."
            )

        # Return the improved content.
        return {
            "content": content
        }


    # Execute the graph.
    def run(self, topic: str):

        initial_state = { "topic": topic  }
        return self.app.invoke(initial_state)
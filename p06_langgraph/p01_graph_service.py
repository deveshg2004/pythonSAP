
# Import StateGraph to create our graph workflow.
# Import START and END to define the beginning and end of execution.
from langgraph.graph import StateGraph, START, END

# Import our custom state structure.
from p01_state import GraphState


class GraphService:

    def __init__(self):

        self.graph_builder = StateGraph(GraphState)

        self.graph_builder.add_node( "process_input",  self.process_input   )
        self.graph_builder.add_node(  "generate_response",   self.generate_response )


        self.graph_builder.add_edge(  START, "process_input"  )
        self.graph_builder.add_edge(  "process_input", "generate_response" )
        self.graph_builder.add_edge( "generate_response", END  )

        self.graph = self.graph_builder.compile()



    # Define the first node to clean the user input.
    def process_input(self, state: GraphState):

        print("\n[Node 1] Processing user input...")

        user_input = state["user_input"]
        cleaned_text = user_input.strip().title()

        print("[Node 1] Input processed successfully.")

        return { "cleaned_input": cleaned_text }



    def generate_response(self, state: GraphState):

        print("\n[Node 2] Generating response...")

        cleaned_text = state["cleaned_input"]
        final_response = f"Welcome to {cleaned_text}!"

        print("[Node 2] Response generated successfully.")

        return { "response": final_response }



    # Define a method to execute the compiled graph.
    def run_graph(self, user_input: str):

        initial_state = {  "user_input": user_input  }
        result = self.graph.invoke(initial_state)
        return result

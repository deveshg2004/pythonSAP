
# Import TypedDict to define the structure of our graph state.
from typing_extensions import TypedDict


# Define the state structure used throughout the graph.
class GraphState(TypedDict):

    user_input: str
    cleaned_input: str
    response: str

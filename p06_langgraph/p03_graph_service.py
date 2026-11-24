from langgraph.graph import StateGraph, START, END

from p06_langgraph.p03_state import SupportState


class CustomerSupportGraph:

    def __init__(self):

        self.graph = StateGraph(SupportState)

        # Register all the nodes in the graph.
        self.graph.add_node("classify_query", self.classify_query)
        self.graph.add_node("billing_support", self.billing_support)
        self.graph.add_node("technical_support", self.technical_support)
        self.graph.add_node("general_support", self.general_support)


        self.graph.add_edge(START, "classify_query")

        # Add conditional routing after the classification node.
        self.graph.add_conditional_edges( "classify_query",
            self.route_query,
            {
                "billing": "billing_support",
                "technical": "technical_support",
                "general": "general_support"
            }
        )

        # Connect each support node to END.
        self.graph.add_edge("billing_support", END)
        self.graph.add_edge("technical_support", END)
        self.graph.add_edge("general_support", END)

        self.app = self.graph.compile()


    # Node 1: Identify the category of the customer query.
    def classify_query(self, state: SupportState):

        query = state["user_query"].lower()

        billing_keywords = [ "salary", "payment","invoice",  "bill", "refund",  "transaction" ]

        technical_keywords = [ "error", "bug", "not working", "application", "login", "password"]


        if any(word in query for word in billing_keywords):
            return {"category": "billing"}

        elif any(word in query for word in technical_keywords):
            return {"category": "technical"}

        else:

            return {"category": "general"}


    # Routing function: Decide which node should execute next.
    def route_query(self, state: SupportState):

        category = state["category"]

        # Return the route corresponding to the category.
        if category == "billing":
            return "billing"

        elif category == "technical":
            return "technical"

        # Route all other categories to general support.
        return "general"



    # Node 2: Handle billing-related queries.
    def billing_support(self, state: SupportState):

        # Prepare a billing department response.
        response = (
            "Your query has been forwarded to the Billing Department. "
            "They will assist you with payment, invoice or salary-related issues."
        )

        # Return the department and response as state updates.
        return {
            "department": "Billing Department",
            "response": response
        }


    # Node 3: Handle technical queries.
    def technical_support(self, state: SupportState):

        # Prepare a technical support response.
        response = (
            "Your query has been forwarded to Technical Support. "
            "They will assist you with application, login or technical issues."
        )

        # Return the department and response as state updates.
        return {
            "department": "Technical Support",
            "response": response
        }


    # Node 4: Handle general queries.
    def general_support(self, state: SupportState):

        # Prepare a general support response.
        response = (
            "Your query has been forwarded to General Support. "
            "They will assist you with general information and enquiries."
        )

        # Return the department and response as state updates.
        return {
            "department": "General Support",
            "response": response
        }


    # Execute the compiled graph with the customer's query.
    def run(self, user_query: str):

        # Create the initial state.
        initial_state = {  "user_query": user_query  }

        return self.app.invoke(initial_state)
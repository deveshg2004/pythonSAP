from p06_langgraph.p03_graph_service import CustomerSupportGraph

support_system = CustomerSupportGraph()

user_query = input("Enter your support query: ")

result = support_system.run(user_query)

print("\nCustomer Query:", result["user_query"])

print("Detected Category:", result["category"])

print("Assigned Department:", result["department"])

print("\nSupport Response:")
print(result["response"])
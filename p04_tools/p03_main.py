
from p03_agent import AIAgent

agent = AIAgent()

user_query = input("\nAsk your AI Agent: ")
response = agent.run(user_query)

print("\nFinal AI Response:")
print(response)


from p02_llm_tool_calling import ToolCallingService

tool_service = ToolCallingService()

user_query = input("\nAsk me something: ")

response = tool_service.process_query(user_query)

print("\nAI Response:", response)

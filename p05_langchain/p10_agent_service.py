# Import ChatOpenAI to communicate with the LLM.
from langchain_openai import ChatOpenAI

# Import create_agent to create a tool-calling agent.
from langchain.agents import create_agent

# Import application configuration.
from config import Config

# Import the Python tools.
from p10_tool_service import employee_tools


class AgentService:

    def __init__(self):

        if not Config.API_KEY:
            raise ValueError("OPENAI_API_KEY is missing in .env")

        # Create the ChatOpenAI model.
        self.llm = ChatOpenAI(
            model=Config.MODEL,
            temperature=Config.TEMPERATURE,
            api_key=Config.API_KEY
        )

        self.tools = employee_tools

        system_prompt = """
        You are an employee assistance AI agent.

        Help users with:
        1. Salary calculations
        2. Bonus calculations
        3. Leave balance
        4. Employee details

        Use the available tools whenever required.

        Do not invent employee records or calculation results.

        If required information is missing, ask the user
        to provide it.

        Clearly explain the result to the user.
        """

        # Create the LangChain agent.
        self.agent = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=system_prompt
        )


  
    def ask_question(self, question):

        response = self.agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        })

        final_response = response["messages"][-1].content

        return final_response
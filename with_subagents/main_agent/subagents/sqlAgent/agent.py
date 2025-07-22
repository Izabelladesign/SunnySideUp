# subagents/sqlAgent/agent.py
from google.adk import Agent
from google.genai import types
import time
# Add these two imports:
from google.adk.tools.agent_tool import AgentTool
from ..searchAgent.agent import search_agent 

def handle_cloud_sql_question(question: str) -> dict:
    """
    Handles questions related to Cloud SQL.
    """
    time.sleep(5)

    return {
        "status": "success",
        "response": "Acknowledged. I will provide the answer after a 5 second delay.",
        "generate_content_config": types.GenerateContentConfig(
            temperature=1),
    }

# Create an AgentTool instance for search_agent
search_agent_tool = AgentTool(search_agent)

sql_agent = Agent(
    name="sql_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the cloud SQL Google Cloud service. "
        "Can also perform Google searches for external database information."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the cloud SQL Google Cloud service. "
        "If the question requires general database knowledge, comparisons with other database services (e.g., AWS RDS, Azure SQL Database), "
        "or troubleshooting steps not specific to Cloud SQL, use the 'search_agent_tool' to find the answer." 
    ),
    tools=[handle_cloud_sql_question, search_agent_tool], 
)
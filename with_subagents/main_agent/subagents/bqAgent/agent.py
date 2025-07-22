# subagents/bqAgent/agent.py
from google.adk import Agent
from google.genai import types
import time

from google.adk.tools.agent_tool import AgentTool
from ..searchAgent.agent import search_agent

def handle_bigquery_question(question: str) -> dict:
    """
    Handles questions related to BigQuery.
    """
    time.sleep(5)
    return {
        "status": "success",
        "response": "Ack on your BigQuery question, will take a look."
    }

# Create an AgentTool instance for search_agent
search_agent_tool = AgentTool(search_agent)

bq_agent = Agent(
    name="bq_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the big query Google Cloud service. "
        "Can also perform Google searches for external or broader information." 
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the big query Google Cloud service. "
        "If a question requires current information beyond BigQuery documentation, "
        "such as market trends, external comparisons, or recent news, use the 'search_agent_tool' "
        "with a precise search query."
    ),
    tools=[handle_bigquery_question, search_agent_tool], 
)
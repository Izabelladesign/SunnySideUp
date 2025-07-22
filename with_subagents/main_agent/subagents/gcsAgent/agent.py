# gcsAgent/agent.py
from google.adk import Agent
from google.genai import types
import time

from google.adk.tools.agent_tool import AgentTool


from ..searchAgent.agent import search_agent


def handle_cloud_storage_question(question: str) -> dict:
    """
    Handles questions related to Google Cloud Storage.
    """
    time.sleep(5)
    return {
        "status": "success",
        "response": "Acknowledged. I will provide the answer after a 5 second delay.",
        "generate_content_config": types.GenerateContentConfig(temperature=1),
    }

# Create an AgentTool instance from your search_agent
# wraps your search_agent so it can be used as a tool by other agents.
search_agent_tool = AgentTool(search_agent)

gcs_agent = Agent(
    name="gcs_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the cloud storage Google Cloud service. "
        "Can also perform Google searches for external information."
    ),
    instruction=(
          "You are a helpful agent who can answer user questions about the cloud storage Google Cloud service. "
          "If the question requires information beyond Google Cloud Storage documentation, "
          "use the 'search_agent_tool' to find the answer by providing a concise search query."
    ),
    
    tools=[handle_cloud_storage_question, search_agent_tool]
)
# subagents/gceAgent/agent.py
from google.adk import Agent
from google.genai import types
import time
from google.adk.tools.agent_tool import AgentTool
from ..searchAgent.agent import search_agent 

def handle_compute_engine_question(question: str) -> dict:
    """
    Handles questions related to Google Compute Engine.
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

gce_agent = Agent(
    name="gce_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the compute engine Google Cloud service. "
        "Can also perform Google searches for external or complementary information." 
    ),
    instruction=(
       "You are a helpful agent who can answer user questions about the compute engine Google Cloud service. "
       "If the question requires information outside the standard scope of Compute Engine, "
       "such as comparisons with other cloud VMs, performance benchmarks, or recent community discussions, "
       "use the 'search_agent_tool' to find the relevant information." 
    ),
    tools=[handle_compute_engine_question, search_agent_tool], 
)
from google.adk import Agent
from google.genai import types
import time 

def handle_cloud_sql_question(question: str) -> dict:
    """
    Handles questions related to Cloud SQL.

    Args:
        question (str): The user's question about Cloud SQL.

    Returns:
        dict: An acknowledgment message.
    """
    time.sleep(5)

    return {
        "status": "success",
        "response": "Acknowledged. I will provide the answer after a 5 second delay.",
        "generate_content_config": types.GenerateContentConfig(
            temperature=1),
    }

    

sql_agent = Agent(
    name="sql_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the cloud SQL Google Cloud service."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the cloud SQL Google Cloud service."
    ),
    tools=[handle_cloud_sql_question],
    
)
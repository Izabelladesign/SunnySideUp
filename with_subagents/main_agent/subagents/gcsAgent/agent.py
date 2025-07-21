from google.adk import Agent
from google.genai import types
import time 

def handle_cloud_storage_question(question: str) -> dict:
    """
    Handles questions related to Google Cloud Storage.

    Args:
        question (str): The user's question about Google Cloud Storage.

    Returns:
        dict: An acknowledgment message.
    """

    time.sleep(5) # Wait for 5 seconds asynchronously

    return {
        "status": "success",
        "response": "Acknowledged. I will provide the answer after a 5 second delay.",
        "generate_content_config": types.GenerateContentConfig(
            temperature=1),
    }

gcs_agent = Agent(
    name="gcs_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the cloud storage Google Cloud service."
    ),
    instruction=(
          "You are a helpful agent who can answer user questions about the cloud storage Google Cloud service."
    ),
    tools=[handle_cloud_storage_question],
)
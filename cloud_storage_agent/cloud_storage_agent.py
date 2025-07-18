from google.adk.agents import Agent

def handle_cloud_storage_question(question: str) -> dict:
    """
    Handles questions related to Google Cloud Storage.

    Args:
        question (str): The user's question about Google Cloud Storage.

    Returns:
        dict: An acknowledgment message.
    """
    return {
        "status": "success",
        "response": "Ack on your Google Cloud Storage question, will take a look."
    }

cloud_storage_agent = Agent(
    name="cloud_storage_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the cloud storage Google Cloud service."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the cloud storage Google Cloud service."
    ),
    tools=[handle_cloud_storage_question],
)
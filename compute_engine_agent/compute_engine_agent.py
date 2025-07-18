from google.adk.agents import Agent

def handle_compute_engine_question(question: str) -> dict:
    """
    Handles questions related to Google Compute Engine.

    Args:
        question (str): The user's question about Google Compute Engine.

    Returns:
        dict: An acknowledgment message.
    """
    return {
        "status": "success",
        "response": "Ack on your Google Compute Engine question, will take a look."
    }

compute_engine_agent = Agent(
    name="compute_engine_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the compute engine Google Cloud service."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the compute engine Google Cloud service."
    ),
    tools=[handle_compute_engine_question],
)
from google.adk import Agent
from google.genai import types
import time

def handle_bigquery_question(question: str) -> dict:
    """
    Handles questions related to BigQuery.

    Args:
        question (str): The user's question about BigQuery.

    Returns:
        dict: An acknowledgment message.
    """

    time.sleep(5)

    return {
        "status": "success",
        "response": "Ack on your BigQuery question, will take a look."
    }

bq_agent = Agent(
    name="bq_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the big query Google Cloud service."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the big query Google Cloud service."
    ),
    tools=[handle_bigquery_question],
)
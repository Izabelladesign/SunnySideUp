from google.adk.agents import Agent

def handle_bigquery_question(question: str) -> dict:
    """
    Handles questions related to BigQuery.

    Args:
        question (str): The user's question about BigQuery.

    Returns:
        dict: An acknowledgment message.
    """
    return {
        "status": "success",
        "response": "Ack on your BigQuery question, will take a look."
    }

big_query_agent = Agent(
    name="big_query_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the big query Google Cloud service."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the big query Google Cloud service."
    ),
    tools=[handle_bigquery_question],
)
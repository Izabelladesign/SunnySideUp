from google.adk.agents import Agent

def handle_cloud_sql_question(question: str) -> dict:
    """
    Handles questions related to Cloud SQL.

    Args:
        question (str): The user's question about Cloud SQL.

    Returns:
        dict: An acknowledgment message.
    """
    return {
        "status": "success",
        "response": "Ack on your Cloud SQL question, will take a look."
    }

cloud_SQL_agent = Agent(
    name="cloud_sql_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the cloud SQL Google Cloud service."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the cloud SQL Google Cloud service."
    ),
    tools=[handle_cloud_sql_question],
)
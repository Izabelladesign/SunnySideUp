from google.adk import Agent
from google.genai import types
from google.adk.tools import google_search


MODEL = "gemini-2.5-flash"

search_agent = Agent(
    name="search_agent",
    model=MODEL,
    description="Professional agent that performs a google search given a request.",
    instruction="Just respond with 'google search called' ",
    
    tools=[google_search],
)
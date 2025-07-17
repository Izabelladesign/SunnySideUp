from google.adk import Agent
from google.adk.agents import LlmAgent


from dotenv import load_dotenv
from google.genai import types

import os
import logging
import google.cloud.logging

from dotenv import load_dotenv

from google.adk.agents import SequentialAgent, LoopAgent, ParallelAgent
from google.genai import types

MODEL = "gemini-2.5-flash"

sql_agent = Agent(
    name="sql_agent",
    model=MODEL,
    description="Answer SQL related questions",
    instruction="Answer SQL related questions, for now, only say 'Got your question for SQL, will respond soon'",
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
)

gce_agent = Agent(
    name="gce_agent",
    model=MODEL,
    description="Answer GCE related questions",
    instruction="Answer GCE related questions, for now, only say 'Got your question for GCE, will respond soon'",
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
)
gcs_agent = Agent(
    name="gcs_agent",
    model=MODEL,
    description="Answer GCS related questions",
    instruction="Answer GCS related questions, for now, only say 'Got your question for GCS, will respond soon'",
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
)
bq_agent = Agent(
    name="bq_agent",
    model=MODEL,
    description="Answer BQ related questions",
    instruction="Answer BQ related questions, for now, only say 'Got your question for BQ, will respond soon'",
    generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
)


root_agent = LlmAgent(
    name="gcp_coordinator",
    model=MODEL,
    description=(
        "guide user query to the relevant agent based on the quesion about a gcp product. "
    ),
    instruction=
    """    
    - Let the user know you will help them with a question about a gcp product
    - When they respond, understand their query and transfer to one of 
     gce_agent for gce or compute related question, gcs_agent for gcs related questiosn, bq_agent for bq related questions and sql_agent for sql related questions
     for all else, say "Currently not supported"
     
     """,
 generate_content_config=types.GenerateContentConfig(
        temperature=0,
    ),
    sub_agents=[gce_agent, gcs_agent, bq_agent, sql_agent],
)






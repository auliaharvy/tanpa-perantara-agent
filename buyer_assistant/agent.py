"""Agent module for the Tata Buyer Assistant."""

from google.adk import Agent
from google.adk.tools import AgentTool
from .prompts import INSTRUCTION
from .sub_agents.database_agent import database_agent
from .sub_agents.web_search_agent import web_search_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='tata_property_agent',
    description='A helpful property sales assistant named Tata.',
    instruction=INSTRUCTION,
    tools=[AgentTool(database_agent), AgentTool(web_search_agent)]
)
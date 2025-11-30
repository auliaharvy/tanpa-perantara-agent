import os
from google.adk.agents import LlmAgent
from .. import prompts
from toolbox_core import ToolboxSyncClient

# Connect to the running toolbox instance
toolbox_url = os.getenv('TOOLBOX_URL', 'http://127.0.0.1:5000')
client = ToolboxSyncClient(toolbox_url)
tools = client.load_toolset('property_tools')

database_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='database_retrieval_agent',
    description='Agen khusus untuk mengambil data properti dari database PostgreSQL internal.',
    instruction=prompts.DATABASE_RETRIEVAL_AGENT_INSTRUCTION,
    tools=tools
)

from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .. import prompts

web_search_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='web_search_agent',
    description='Agen yang melakukan pencarian web untuk data investasi properti.',
    instruction=prompts.WEB_SEARCH_AGENT_INSTRUCTION,
    tools=[google_search]
)

from google.adk.agents import LlmAgent
from google.adk.tools import    
from .. import prompts

web_search_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='web_search_agent',
    description='Agen khusus untuk mencari sentimen pasar dan berita eksternal.',
    instruction=prompts.WEB_SEARCH_AGENT_INSTRUCTION,
    tools=[google_search]
)

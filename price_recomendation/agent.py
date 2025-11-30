import asyncio
import json
from google.adk.agents import LlmAgent
from google.adk.tools import AgentTool
from google.adk.runners import InMemoryRunner
from google.genai.types import Part, UserContent

from .sub_agents.database_agent import database_agent
from .sub_agents.web_search_agent import web_search_agent
from . import prompts

# ==========================================
# DEFINISI ROOT AGENT
# ==========================================

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='property_valuation_root_agent',
    description='Agen utama yang mengoordinasikan penilaian properti.',
    instruction=prompts.ROOT_AGENT_INSTRUCTION,
    tools=[
        AgentTool(database_agent),
        AgentTool(web_search_agent)
    ]
)

# ==========================================
# EKSEKUSI (FLOW)
# ==========================================

async def main():
    # 1. Input User (JSON)
    user_input_data = {
        "luas_tanah": 100,
        "lokasi": "Bintaro Sektor 9",
        "kamar": 3
    }
    
    # Konversi dict ke format TOON (YAML-like) agar lebih token-efficient
    # Format: key: value
    toon_input = "\n".join([f"{k}: {v}" for k, v in user_input_data.items()])
    
    prompt_user = f"Analisa properti ini (Data dalam format TOON):\n```toon\n{toon_input}\n```"

    print("--- AGENT SYSTEM STARTED ---")
    
    # 2. Inisialisasi Runner
    runner = InMemoryRunner(agent=root_agent)
    
    # 3. Buat Session
    session = await runner.session_service.create_session(
        app_name=runner.app_name, user_id="test_user"
    )
    
    # 4. Siapkan Konten User
    content = UserContent(parts=[Part(text=prompt_user)])
    
    final_text_response = ""
    
    # 5. Jalankan Agent
    print("Processing...", end="", flush=True)
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        # print(f"\nEvent: {event}") # Debugging
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    final_text_response += part.text
                    print(".", end="", flush=True)

    print("\n\n--- FINAL OUTPUT ---")
    
    # Membersihkan output jika ada markdown block
    clean_response = final_text_response.replace("```json", "").replace("```", "").strip()
    
    try:
        final_json = json.loads(clean_response)
        print(json.dumps(final_json, indent=4))
    except json.JSONDecodeError:
        print("Raw Response:", final_text_response)

if __name__ == "__main__":
    asyncio.run(main())
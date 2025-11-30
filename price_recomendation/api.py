import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.adk.runners import InMemoryRunner
from google.genai.types import Part, UserContent
from price_recomendation.agent import root_agent

app = FastAPI(title="Property Valuation Agent API")

class PropertyInput(BaseModel):
    lokasi: str
    luas_tanah: int
    kamar: int
    # Tambahkan field lain sesuai kebutuhan, misal:
    # luas_bangunan: int | None = None

@app.post("/analyze")
async def analyze_property(data: PropertyInput):
    """
    Menerima data properti dalam format JSON, mengubahnya ke TOON,
    dan mengirimkannya ke Agent untuk dianalisa.
    """
    try:
        # 1. Konversi Input ke Dictionary
        input_dict = data.model_dump()
        
        # 2. Konversi ke Format TOON (YAML-like)
        toon_input = "\n".join([f"{k}: {v}" for k, v in input_dict.items()])
        prompt_user = f"Analisa properti ini (Data dalam format TOON):\n```toon\n{toon_input}\n```"
        
        print(f"\n[API] Received Request: {input_dict}")
        print(f"[API] Sending to Agent (TOON):\n{toon_input}")

        # 3. Inisialisasi Runner & Session
        # Note: Untuk production, sebaiknya reuse runner/session atau manage session lifecycle lebih baik
        runner = InMemoryRunner(agent=root_agent)
        session = await runner.session_service.create_session(
            app_name=runner.app_name, user_id="api_user"
        )
        
        # 4. Kirim Pesan ke Agent
        content = UserContent(parts=[Part(text=prompt_user)])
        final_text_response = ""
        
        async for event in runner.run_async(
            user_id=session.user_id,
            session_id=session.id,
            new_message=content,
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        final_text_response += part.text

        # 5. Bersihkan & Parse Output JSON Agent
        clean_response = final_text_response.replace("```json", "").replace("```", "").strip()
        
        try:
            final_json = json.loads(clean_response)
            return final_json
        except json.JSONDecodeError:
            # Jika agent gagal return JSON valid, return raw text tapi dengan status error 500 atau warning
            print(f"[API ERROR] Invalid JSON from Agent: {final_text_response}")
            raise HTTPException(status_code=500, detail="Agent failed to produce valid JSON output. Raw response: " + final_text_response)

    except Exception as e:
        print(f"[API ERROR] {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

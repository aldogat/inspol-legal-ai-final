from fastapi import APIRouter, HTTPException
from openai import OpenAI
import os

router = APIRouter()

@router.post("/multimodal")
@router.post("/mensaje")
async def simple_chat(data: dict):
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        # Acepta tanto "message" como "messages" para máxima compatibilidad
        msg = data.get("message") or (data.get("messages") or [{}])[0].get("content", "")
        if not msg:
            raise HTTPException(status_code=400, detail="No message provided")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": msg}],
            max_tokens=1024
        )
        return {"reply": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

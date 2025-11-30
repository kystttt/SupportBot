from my_settings_env import OPENROUTER_API_KEY
import httpx

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "x-ai/grok-4.1-fast:free"

SYSTEM_PROMPT = """
Ты ассистент техподдержки по продукту пластиковые окна.
Отвечай только по продукту, без мата и оскорблений.
Если вопрос не по теме — вежливо скажи, что отвечаешь только по продукту пластиковые окна.
"""

async def ask_llm(user_message: str) -> str:
    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message},
                ],
                "temperature": 0.1,
                "max_tokens": 500,
            },
        )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip()
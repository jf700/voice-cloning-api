import os
import httpx
from app.config import settings

CARTESIA_API_KEY = settings.CARTESIA_API_KEY
CARTESIA_BASE_URL = settings.CARTESIA_BASE_URL
HEADERS = {"Authorization": f"Bearer {CARTESIA_API_KEY}"}


async def synthesize_speech(synthesis_request):
    payload = {
        "text": synthesis_request.text,
        "voiceId": str(synthesis_request.voiceId),
        "emotion": getattr(synthesis_request, "emotion", "neutral"),
        "speed": getattr(synthesis_request, "speed", "normal"),
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{CARTESIA_BASE_URL}/speak", json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.content  # This returns raw audio data

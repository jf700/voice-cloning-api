from app.clients.cartesia_client import CartesiaClient
from app.config import settings

cartesia_client = CartesiaClient(api_key=settings.CARTESIA_API_KEY)

async def list_voices():
    return await cartesia_client.list_voices()

async def get_voice(voice_id):
    return await cartesia_client.get_voice(voice_id)

async def create_voice_clone(voice_data):
    return await cartesia_client.create_voice_clone(
        source_id=voice_data["sourceId"],
        name=voice_data["name"],
        description=voice_data["description"],
        mode=voice_data.get("mode", "stability"),
        source_type=voice_data.get("sourceType", "upload")
    )

async def get_voice_samples(voice_id):
    return await cartesia_client.get_voice_samples(voice_id)

async def delete_voice(voice_id):
    return await cartesia_client.delete_voice(voice_id)

async def synthesize(req_data):
    return await cartesia_client.synthesize(
        text=req_data["text"],
        voice_id=req_data["voiceId"],
        emotion=req_data.get("emotion", "neutral"),
        speed=req_data.get("speed", "normal")
    )

from fastapi.responses import StreamingResponse
from app.models.schemas import SynthesisRequest, SynthesisBatchRequest, SynthesisBatchStatusResponse
from io import BytesIO
import uuid
import random
import datetime

# Simulate a voice synthesis service
async def synthesize(req: SynthesisRequest):
    audio_data = BytesIO(b"FAKE_MP3_AUDIO")
    return StreamingResponse(audio_data, media_type="audio/mpeg")

# Simulate batch synthesis request
async def synthesize_batch(req: SynthesisBatchRequest):
    batch_id = str(uuid.uuid4())
    return {"batchId": batch_id}

# Simulate polling a batch job
async def get_batch_status(batch_id: uuid.UUID):
    return SynthesisBatchStatusResponse(
        batchId=batch_id,
        status="completed",
        progress=100,
        items=[
            {
                "outputId": str(uuid.uuid4()),
                "status": "completed",
                "downloadUrl": "https://example.com/audio.mp3",
                "error": None
            }
        ]
    )

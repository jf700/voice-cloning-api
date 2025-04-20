from datetime import datetime
from fastapi import APIRouter, Query, UploadFile, File, HTTPException, Path
from fastapi.responses import StreamingResponse
from app.models.schemas import (
    UploadedFile, Error,
    Voice, SynthesisRequest, SynthesisBatchRequest,
    SynthesisBatchStatusResponse, VoiceSample,
)
from uuid import UUID
from app.services import voice_service, synthesis_service

router = APIRouter(tags=["Voice"])

@router.post("/upload", response_model=UploadedFile)
async def upload_file(file: UploadFile = File(...)):
    return await voice_service.upload_file(file)

@router.post("/voices", response_model=VoiceSample)
async def create_voice(req: Voice):
    return await voice_service.create_voice(req)

@router.get("/voices/{voice_id}", response_model=VoiceSample)
async def get_voice(voice_id: UUID):
    return await voice_service.get_voice(voice_id)

@router.post("/synthesis", response_class=StreamingResponse)
async def synthesize(req: SynthesisRequest):
    return await synthesis_service.synthesize(req)

@router.post("/synthesis/batch", response_model=dict)
async def synthesize_batch(req: SynthesisBatchRequest):
    return await synthesis_service.synthesize_batch(req)

@router.get("/synthesis/batch/{batch_id}", response_model=SynthesisBatchStatusResponse)
async def get_batch_status(batch_id: UUID):
    return await synthesis_service.get_batch_status(batch_id)

voice_db = {}

@router.get("/voices", response_model=dict)
async def list_voices(limit: int = Query(20), offset: int = Query(0)):
    voices = list(voice_db.values())[offset:offset+limit]
    return {
        "voices": voices,
        "total": len(voice_db)
    }

@router.delete("/voices/{voiceId}", status_code=204)
async def delete_voice(voiceId: UUID = Path(...)):
    if str(voiceId) in voice_db:
        del voice_db[str(voiceId)]
        return
    raise HTTPException(status_code=404, detail="Voice not found")

# Simulated voice samples
voice_samples = {
    "some-uuid": [
        VoiceSample(
            id=UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
            text="Hello world!",
            audioUrl="https://example.com/audio.mp3",
            created=datetime.utcnow(),
            duration=2.3,
            speed="normal",
            emotion="neutral"
        )
    ]
}

@router.get("/voices/{voiceId}/samples", response_model=dict)
async def get_voice_samples(voiceId: UUID):
    samples = voice_samples.get(str(voiceId), [])
    return {"samples": samples}
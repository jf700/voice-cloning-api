from datetime import datetime, timedelta
import boto3
from fastapi import APIRouter, Query, UploadFile, File, HTTPException, Path
from fastapi.responses import StreamingResponse
from app.models.schemas import (
    UploadedFile, Error,
    Voice, SynthesisRequest, SynthesisBatchRequest,
    SynthesisBatchStatusResponse, VoiceSample, VoiceCloneRequest,
)
from uuid import UUID, uuid4
from app.services import voice_service, synthesis_service
from app.services.transcription_service import transcribe_s3_audio

router = APIRouter(tags=["Voice"])

s3 = boto3.client("s3")
BUCKET = "voicecloningtest"
sessions = {}

@router.post("/upload", response_model=UploadedFile)
async def upload_to_s3(file: UploadFile, prefix="samples"):
    file_id = str(uuid4())
    key = f"{prefix}/{file_id}_{file.filename}"
    content = await file.read()
    s3.put_object(Bucket=BUCKET, Key=key, Body=content, ContentType=file.content_type)
    return {"filename": file.filename, "key": key}

@router.post("/record")
async def start_recording():
    session_id = uuid4()
    now = datetime.utcnow()
    expires = now + timedelta(minutes=10)
    sessions[str(session_id)] = {
        "status": "recording",
        "duration": 0.0,
        "createdAt": now,
        "expiresAt": expires,
        "fileId": str(session_id),
    }
    return {
        "sessionId": session_id,
        "websocketUrl": f"wss://mock-recording-service/{session_id}",
        "expiresAt": expires,
        "maxDuration": 10.0
    }

@router.get("/record/{sessionId}")
async def get_recording_status(sessionId: UUID):
    session = sessions.get(str(sessionId))
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {
        "sessionId": str(sessionId),
        "status": session["status"],
        "duration": session["duration"],
        "fileId": session["fileId"],
        "error": None
    }

@router.delete("/record/{sessionId}")
async def cancel_recording(sessionId: UUID):
    if str(sessionId) in sessions:
        del sessions[str(sessionId)]
        return {}, 204
    raise HTTPException(status_code=404, detail="Session not found")



@router.get("/voices")
async def list_voices():
    return await voice_service.list_voices()


@router.post("/voices/clone")
async def create_voice_clone(req: VoiceCloneRequest):
    return await voice_service.create_voice_clone(req.dict())




@router.get("/voices/{voice_id}", response_model=VoiceSample)
async def get_voice(voice_id: UUID):
    return await voice_service.get_voice(voice_id)

@router.delete("/voices/{voiceId}", status_code=204)
async def delete_voice(voiceId: UUID = Path(...)):
    if str(voiceId) in voice_db:
        del voice_db[str(voiceId)]

@router.get("/voices/{voice_id}/samples")
async def get_voice_samples(voice_id: UUID):
    # This assumes the method is implemented in voice_service
    return await voice_service.get_voice_samples(str(voice_id))

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


import uuid
from datetime import datetime, timedelta
from fastapi import UploadFile
from app.models.schemas import Voice, VoiceSample, UploadedFile

async def upload_file(file: UploadFile):
    now = datetime()
    return UploadedFile(
        fileId=uuid.uuid4(),
        fileName=file.filename,
        fileSize=1024,
        duration=3.5,
        uploadedAt=now,
        expiresAt=now + timedelta(days=1)
    )

async def create_voice(req: Voice):
    now = datetime()
    return VoiceSample(
        id=uuid.uuid4(),
        name=req.name,
        description=req.description,
        mode=req.mode,
        created=now,
        lastUsed=now,
        status="processing",
        sampleUrl="https://fake-audio-url.com/sample.mp3"
    )

async def get_voice(voice_id):
    now = datetime()
    return VoiceSample(
        id=voice_id,
        name="Sample Voice",
        description="Auto-generated voice",
        mode="stability",
        created=now,
        lastUsed=now,
        status="ready",
        sampleUrl="https://fake-audio-url.com/sample.mp3"
    )

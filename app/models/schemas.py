from pydantic import BaseModel, Field
from uuid import UUID
from typing import List, Optional
from enum import Enum
from datetime import datetime

class UploadedFile(BaseModel):
    id: UUID
    fileName: str
    fileSize: int
    mimeType: str
    duration: float
    createdAt: datetime
    expiresAt: datetime

class VoiceCloneRequest(BaseModel):
    sourceType: str = "upload"
    sourceId: str
    name: str
    description: str
    mode: str = "stability"
    
class RecordingStatus(str, Enum):
    waiting = "waiting"
    recording = "recording"
    processing = "processing"
    completed = "completed"
    failed = "failed"
    cancelled = "cancelled"

class RecordingSession(BaseModel):
    id: UUID
    status: RecordingStatus
    duration: float
    createdAt: datetime
    expiresAt: datetime
    fileId: Optional[UUID]

class VoiceStatus(str,Enum):
    processing = "processing"
    ready = "ready"
    failed = "failed"

class Mode(str, Enum):
    stability = "stability"
    synthesis = "syntheis"

class Voice(BaseModel):
    name: str
    description: str
    embedding: List[float]  # list of 192 floats
    language: Optional[str] = None
    base_voice_id: Optional[str] = None

class Speed(str, Enum):
    slow = "slow"
    normal = "normal"
    fast = "fast"
    fastest = "fastest"

class Emotion (str, Enum):
    anger = "anger"
    positivity = "positivity"
    suprise = "suprise"
    sadness = "sadness"
    curiosity = "curiosity"
    neutral = "neutral"

class VoiceSample(BaseModel):
    id: UUID
    text: str
    audioUrl: str
    created: datetime
    duration: float
    speed: Speed
    emotion: Emotion

class Error(BaseModel):
    code: str
    message: str
    details: Optional[dict]


class SynthesisRequest(BaseModel):
    voiceId: UUID
    text: str
    speed: Optional[str] = "normal"
    emotion: Optional[str] = "neutral"
    format: Optional[str] = "mp3"

class SynthesisBatchRequest(BaseModel):
    items: List[SynthesisRequest]
    format: str

class SynthesisBatchStatusResponse(BaseModel):
    batchId: UUID
    status: str
    progress: int
    items: List[dict]

class UsageDayStat(BaseModel):
    date: str
    characters: int
    audioSeconds: int

class UsagePeriod(BaseModel):
    startDate: str
    endDate: str

class UsageResponse(BaseModel):
    period: UsagePeriod
    totalCharacters: int
    totalAudioSeconds: int
    voiceCreations: int
    usageByDay: List[UsageDayStat]
from fastapi import APIRouter
from app.models.schemas import SynthesisRequest, SynthesisBatchRequest, SynthesisBatchStatusResponse
from app.services import synthesis_service
from uuid import UUID

router = APIRouter(tags=["Synthesis"])

@router.post("/synthesis", operation_id="synthesizeAudio")
async def synthesize(req: SynthesisRequest):
    return await synthesis_service.synthesize(req)

@router.post("/synthesis/batch", operation_id="synthesizeBatch")
async def synthesize_batch(req: SynthesisBatchRequest):
    return await synthesis_service.synthesize_batch(req)

@router.get("/synthesis/batch/{batch_id}", response_model=SynthesisBatchStatusResponse, operation_id="getSynthesisBatchStatus")
async def get_batch_status(batch_id: UUID):
    return await synthesis_service.get_batch_status(batch_id)


from fastapi import APIRouter, HTTPException
from uuid import UUID, uuid4
from datetime import datetime, timedelta

router = APIRouter(tags=["Voice"])

# Simulated session storage
sessions = {}

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

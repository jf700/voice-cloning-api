from fastapi import FastAPI
from app.controllers.voice_controller import router as voice_router
from app.controllers.synthesis_controller import router as synthesis_router
from app.controllers.account_controller import router as account_router


app = FastAPI(
    title="Voice Cloning API",
    version="1.0.0",
    description="API for voice cloning with stability and similarity modes."
)


app.include_router(voice_router)
app.include_router(synthesis_router)
app.include_router(account_router)

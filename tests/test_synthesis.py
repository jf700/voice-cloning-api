import pytest
from app.services.synthesis_service import synthesize_speech
from types import SimpleNamespace

@pytest.mark.asyncio
async def test_synthesize_success():
    request = SimpleNamespace(
        text="Random Sentence",
        voiceId="valid-voice-id",
        emotion="neutral",
        speed="normal"
    )
    result = await synthesize_speech(request)
    assert isinstance(result, bytes)


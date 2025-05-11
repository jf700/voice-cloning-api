import pytest
from app.services.voice_service import create_voice_clone, list_voices
from app.config import settings

@pytest.mark.asyncio
async def test_list_voices():
    voices = await list_voices()
    assert isinstance(voices, dict)
    assert "data" in voices
    assert isinstance(voices["data"], list)


@pytest.mark.asyncio
async def test_create_voice_invalid_embedding():
    with pytest.raises(Exception):
        await create_voice_clone({
            "name": "Test",
            "description": "Should fail",
            "embedding": [0.1] * 50  # Invalid: should be 192 floats
        })

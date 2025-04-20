import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Voice Cloning API"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Example external service settings
    ELEVEN_LABS_API_KEY: str = os.getenv("ELEVEN_LABS_API_KEY", "")
    STORAGE_BUCKET_NAME: str = os.getenv("STORAGE_BUCKET_NAME", "voice-cloning-temp")
    USE_FAKE_DATA: bool = os.getenv("USE_FAKE_DATA", "true").lower() == "true"

settings = Settings()

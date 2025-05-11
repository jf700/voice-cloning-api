import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Voice Cloning API"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Cartesia-specific
    CARTESIA_API_KEY: str = os.getenv("CARTESIA_API_KEY", "sk_car_JQ7ro8UpK8kPS4OnMdPLI")
    CARTESIA_BASE_URL: str = os.getenv("CARTESIA_BASE_URL", "https://api.cartesia.ai")

    STORAGE_BUCKET_NAME: str = os.getenv("STORAGE_BUCKET_NAME", "voicecloningtest")
    USE_FAKE_DATA: bool = os.getenv("USE_FAKE_DATA", "true").lower() == "true"

settings = Settings()

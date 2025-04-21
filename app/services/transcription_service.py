import whisper, tempfile, boto3, os
from botocore.exceptions import BotoCoreError, ClientError

# S3 client setup
s3 = boto3.client("s3")
BUCKET = os.getenv("STORAGE_BUCKET_NAME")

# Load Whisper model once on import
model = whisper.load_model("base")  # Can use "medium" or "large" for better accuracy

def transcribe_s3_audio(key: str) -> str:
    """
    Downloads an audio file from S3 and transcribes it using OpenAI Whisper.

    Parameters:
        key (str): The S3 object key (path in bucket)

    Returns:
        str: The transcribed text from the audio
    """
    try:
        # Retrieve audio file from S3
        response = s3.get_object(Bucket=BUCKET, Key=key)
        audio_bytes = response["Body"].read()

        # Save to temporary file
        with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp_file:
            tmp_file.write(audio_bytes)
            tmp_file.flush()

            # Transcribe with Whisper
            result = model.transcribe(tmp_file.name)
            return result["text"]

    except (BotoCoreError, ClientError) as e:
        raise RuntimeError(f"Failed to access S3 object '{key}': {e}")
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {e}")

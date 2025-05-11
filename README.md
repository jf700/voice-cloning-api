# Voice Cloning API 

## Features 

- Voice Cloning using Cartesia’s `/voices` endpoint
- Voice Management: list, get, delete, patch, localize, mix
- Wrapper Client: `CartesiaClient` encapsulates all Cartesia API calls
- Tests are run using with `pytest`
- I haven't implemented s3 bucket for uploading yet but will later.

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. create `.env`
```bash
CARTESIA_API_KEY="api-key"
CARTESIA_BASE_URL=https://api.cartesia.ai
```

### 3. Run FastAPI server
```bash
uvicorn app.main:app --reload
```

### 4. Open Swagger Docs
To open swagger open
```
http://127.0.0.1:8000/docs
```

## Known Issues

### `synthesize()` fails with 404
the sythesize() method returns a 404 when run with Cartesia Client

I looked in the docs but could not find a synthesize enpoint to use.
## Running Tests

Tests are located in `/tests`.
To run:
```bash
pytest
```

## Project Structure
```
/VoiceCloning
├── app/
│   ├── main.py
│   ├── config.py
│   ├── services/
│   ├── controllers/
│   └── clients/
├── tests/
├── requirements.txt
├── .env
└── README.md
```


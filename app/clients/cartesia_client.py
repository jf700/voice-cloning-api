import httpx

class CartesiaClient:
    def __init__(self, api_key, base_url="https://api.cartesia.ai", version="2024-11-13"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Cartesia-Version": version,
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

    async def list_voices(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/voices/", headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def get_voice(self, voice_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/voices/{voice_id}", headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def create_voice(self, name, description, embedding, language=None, base_voice_id=None):
        payload = {
            "name": name,
            "description": description,
            "embedding": embedding
        }
        if language:
            payload["language"] = language
        if base_voice_id:
            payload["base_voice_id"] = base_voice_id

        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/voices/", json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def create_voice_clone(self, source_id, name, description, mode="stability", source_type="upload"):
        payload = {
            "sourceType": source_type,
            "sourceId": source_id,
            "name": name,
            "description": description,
            "mode": mode
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/voices", json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def delete_voice(self, voice_id):
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"{self.base_url}/voices/{voice_id}", headers=self.headers)
            response.raise_for_status()
            return response.status_code == 204

    async def update_voice(self, voice_id, update_data):
        async with httpx.AsyncClient() as client:
            response = await client.patch(f"{self.base_url}/voices/{voice_id}", json=update_data, headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def localize_voice(self, voice_id, localize_data):
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/voices/{voice_id}/localize", json=localize_data, headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def mix_voices(self, mix_data):
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/voices/mix", json=mix_data, headers=self.headers)
            response.raise_for_status()
            return response.json()

    async def synthesize(self, text, voice_id, emotion="neutral", speed="normal"):
        payload = {
            "text": text,
            "voiceId": voice_id,
            "emotion": emotion,
            "speed": speed
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/speak", json=payload, headers=self.headers)
            response.raise_for_status()
            return response.content

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_voices():
    response = client.get("/voices")
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)


def test_post_voice_clone_missing_params():
    response = client.post("/voices/clone", json={})
    assert response.status_code == 422

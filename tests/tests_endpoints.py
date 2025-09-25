from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 404 


def test_analyze_endpoint():
    response = client.post("/analyze", json={"text": "I am in good mood for a walk"})
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "sarcasm" in data
    assert "sentiment" in data
    assert "toxicity" in data
    assert "emotion" in data
    assert data["text"] == "I am in good mood for a walk"
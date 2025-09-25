from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_sarcasm_endpoint():
    response = client.post("/sarcasm", json={"text": "I am in good mood for a walk"})
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "sarcasm" in data
    assert data["text"] == "I am in good mood for a walk"


def test_sentiment_endpoint():
    response = client.post("/sentiment", json={"text": "I am in good mood for a walk"})
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "sentiment" in data
    assert data["text"] == "I am in good mood for a walk"


def test_toxicity_endpoint():
    response = client.post("/toxicity", json={"text": "I am in good mood for a walk"})
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "toxicity" in data
    assert data["text"] == "I am in good mood for a walk"


def test_emotion_endpoint():
    response = client.post("/emotion", json={"text": "I am in good mood for a walk"})
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "emotion" in data
    assert data["text"] == "I am in good mood for a walk"



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
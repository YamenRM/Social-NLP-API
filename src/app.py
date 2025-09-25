from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import sarcasm_analysis, sentiment_analysis, toxicity_analysis, emotion_analysis

app = FastAPI(title='Social NLP API')

class TextInput(BaseModel):
    text : str


@app.post("/sarcasm")
def sarcasm_endpoint(input: TextInput):
    return {"text": input.text, "sarcasm": sarcasm_analysis(input.text)}


@app.post("/sentiment")
def sentiment_endpoint(input: TextInput):
    return {"text": input.text, "sentiment": sentiment_analysis(input.text)}


@app.post("/toxicity")
def toxicity_endpoint(input: TextInput):
    return {"text": input.text, "toxicity": toxicity_analysis(input.text)}


@app.post("/emotion")
def emotion_endpoint(input: TextInput):
    return {"text": input.text, "emotion": emotion_analysis(input.text)}


# unified endpoint
@app.post("/analyze")
def full_analysis(input: TextInput):
    return {
        "text": input.text,
        "sarcasm": sarcasm_analysis(input.text),
        "sentiment": sentiment_analysis(input.text),
        "toxicity": toxicity_analysis(input.text),
        "emotion": emotion_analysis(input.text),
    }
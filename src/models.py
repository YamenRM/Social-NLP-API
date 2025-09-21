from transformers import pipeline

# Load the models from HF Hub

sarcasm_model = pipeline("text-classification", model="YamenRM/sarcasm_model")
sentiment_model = pipeline("text-classification", model="YamenRM/Sentiment_model")
toxicity_model = pipeline("text-classification", model="YamenRM/Toxicity_model")
emotion_model = pipeline("text-classification", model="YamenRM/Emotion_model")

def get_models():
    return {
        "sarcasm": sarcasm_model,
        "sentiment": sentiment_model,
        "toxicity": toxicity_model,
        "emotion": emotion_model
    }
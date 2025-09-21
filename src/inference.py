from src.models import get_models

models = get_models()

def sarcasm_analysis(text : str):
    return models["sarcasm"](text)[0]
    return {"label": result["label"], "confidence": float(result["score"])}

def sentiment_analysis(text : str):
    return models["sentiment"](text)[0]
    return {"label": result["label"], "confidence": float(result["score"])}

def toxicity_analysis(text : str):
    return models["toxicity"](text)[0]
    return {"label": result["label"], "confidence": float(result["score"])}


def emotion_analysis(text : str):
    return models["emotion"](text)[0]
    return {"label": result["label"], "confidence": float(result["score"])}


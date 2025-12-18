from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Inference API")

class InputData(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    prediction = "positive" if "good" in data.text.lower() else "negative"
    return {
        "prediction": prediction,
        "confidence": 0.9
    }


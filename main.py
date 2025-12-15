from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI()

class InputData(BaseModel):
    features: list

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def inference(data: InputData):
    return {"prediction": predict(data.features)}

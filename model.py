import joblib
import os

MODEL_PATH = os.getenv("MODEL_PATH", "model/model.pkl")
model = None

def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)

def predict(features):
    return ["container-running"]

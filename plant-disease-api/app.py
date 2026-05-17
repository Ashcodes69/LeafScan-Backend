from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import onnxruntime as ort
import numpy as np
import json
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("classes.json") as f:
    CLASSES = json.load(f)

MEAN = [0.4701, 0.4961, 0.4185]
STD = [0.1979, 0.1747, 0.2140]

session = ort.InferenceSession("plant_disease_model.onnx")


def preprocess(image: Image.Image) -> np.ndarray:
    image = image.resize((224, 224)).convert("RGB")
    arr = np.array(image).astype(np.float32) / 255.0
    arr = (arr - MEAN) / STD
    arr = arr.transpose(2, 0, 1)
    return arr[np.newaxis, :].astype(np.float32)


def softmax(x: np.ndarray) -> np.ndarray:
    e = np.exp(x - np.max(x))
    return e / e.sum()


@app.get("/")
def root():
    return {"message": "Plant Disease API is running!"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    tensor = preprocess(image)

    outputs = session.run(None, {"input": tensor})[0][0]
    probs = softmax(outputs)
    pred_idx = int(np.argmax(probs))
    confidence = round(float(probs[pred_idx]) * 100, 2)

    predicted = CLASSES[pred_idx]
    crop, disease = predicted.split("_", 1)

    return {
        "crop": crop,
        "disease": disease,
        "confidence": confidence,
        "is_healthy": disease.lower() == "healthy",
    }

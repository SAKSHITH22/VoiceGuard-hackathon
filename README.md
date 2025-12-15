# VoiceGuard – Dockerized Inference Environment

## 📌 Overview

This project implements a **Dockerized Machine Learning Inference API** using **FastAPI**.
The application exposes REST endpoints for **health checks** and **real-time predictions**, with the ML model loaded safely inside the container.

The goal of this task is to demonstrate the ability to **containerize an inference service** with **clear build and run instructions**, suitable for production and MLOps workflows.

---

## 🛠️ Tech Stack

* **Python 3.10**
* **FastAPI**
* **Uvicorn**
* **Docker**
* **scikit-learn**
* **NumPy**
* **Joblib**

---

## 📂 Project Structure

```
.
├── Dockerfile
├── requirements.txt
├── app
│   ├── main.py        # FastAPI application
│   └── model.py       # Model loading & prediction logic
```

---

## 🚀 API Endpoints

### Health Check

```
GET /health
```

**Response**

```json
{
  "status": "healthy"
}
```

---

### Prediction

```
POST /predict
```

**Request Body**

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

**Response**

```json
{
  "prediction": [0]
}
```

---

## 🐳 Docker Build & Run Instructions

### Build Docker Image

```bash
docker build -t inference-api .
```

### Run Container

```bash
docker run -d -p 8000:8000 --name inference-container inference-api
```

---

## 🧪 Testing the Service

### Health Endpoint

```bash
curl http://localhost:8000/health
```

### Prediction Endpoint

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{"features":[5.1,3.5,1.4,0.2]}'
```

---

## ⚙️ Key Implementation Details

* The ML model is loaded **lazily** to prevent startup crashes
* Docker image uses a **lightweight Python base image**
* API is designed to be **deployment-ready** (Docker, CI/CD, Kubernetes)
* Health endpoint enables monitoring and orchestration readiness

---

## ✅ Task Status

✔ **Task Completed Successfully**
✔ Inference API containerized and tested
✔ Clear build and run instructions provided

---

## 📈 Future Enhancements

* Kubernetes Deployment & Service
* CI/CD pipeline integration
* Model versioning
* Authentication and request validation

---

## 👤 Author

**Sakshith Reddy**
Dockerized Inference Environment – VoiceGuard Task

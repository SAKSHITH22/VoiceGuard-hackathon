# VoiceGuard – Dockerized Inference Environment

## 📌 Overview

This project implements a **Dockerized Machine Learning Inference API** using **FastAPI**.
The application exposes REST endpoints for **health checks** and **real-time predictions**, with the ML model loaded safely inside the container.

The goal of this task is to demonstrate the ability to **containerize an inference service** with **clear build and run instructions**, suitable for production and MLOps workflows.

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.10  
- **Web Framework:** FastAPI  
- **ASGI Server:** Uvicorn  
- **Containerization:** Docker  
- **Base Image:** python:3.10-slim  
- **API Documentation:** Swagger UI (OpenAPI)  
- **Deployment Platform:** AWS EC2 (Dockerized)
---

## 📂 Project Structure

```
.
fastapi-docker/
│── app/
│ └── main.py
│── requirements.txt
│── Dockerfile
│── README.md
```


## 🐳 Docker Build & Run Instructions

### Build Docker Image

```bash
docker build -t fastapi-inference .
```

### Run Container

```bash
docker run -d -p 8000:80 fastapi-inference
```
Container listens on port 80

Application is accessible on port 8000 of the host

### Access the Application

Swagger UI
```bash
http://publicip:8000/docs
```
---

## 🧪 Testing the Service


### Health Check

```
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

### Prediction Endpoint

```
POST /predict
```

Request:

```json
{
  "text": "This is a good example"
}
```

Response:

```json
{
  "prediction": "positive",
  "confidence": 0.9
}
```
---

## ☁️ Deployment Notes (AWS EC2)

* Allow inbound traffic on port **8000** in the EC2 Security Group
* Docker container exposes port **80**
* Uvicorn is bound to `0.0.0.0`

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

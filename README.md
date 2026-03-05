# 🏥 MedVision AI - Diabetic Ulcer Explainable AI Platform

## 🚀 Quick Start - Servers Running!

**Both servers are currently RUNNING:**

- ✅ **Backend API:** http://localhost:8000 (FastAPI + Uvicorn)
- ✅ **Frontend:** http://localhost:5173 (React + Vite)
- ✅ **API Docs:** http://localhost:8000/docs
- ✅ **Health Check:** http://localhost:8000/health

**Deployment Status:** ✅ **READY TO DEPLOY**
- Health check endpoints configured for Render/Heroku
- `render.yaml` Blueprint configuration ready
- Complete deployment guide in [DEPLOYMENT.md](DEPLOYMENT.md)
- Application status in [APPLICATION_STATUS.md](APPLICATION_STATUS.md)

---

## Overview

This project explores how artificial intelligence can assist clinicians in detecting and monitoring **diabetic foot ulcers**.

The goal is to build an **Explainable AI Clinical Decision Support System** that combines **medical image analysis** and **clinical data** to estimate ulcer risk and provide interpretable insights.

The platform is designed as a **full-stack AI application** consisting of:

* **React frontend** for the clinical dashboard
* **FastAPI backend** for APIs and data processing
* **Machine learning pipeline** for prediction and explainability

In addition to predictions, the system generates explanations such as **Grad-CAM heatmaps** and **SHAP feature importance visualizations**.

This project was built to explore modern technologies including **FastAPI, PyTorch, React, Docker, MLflow, and Prometheus monitoring**.

**New Features Added:**
- ✨ Interactive History page with image gallery
- ✨ Enhanced health check endpoints (5 endpoints for monitoring)
- ✨ Chatbot workspace with AI assistant
- ✨ Modern UI with Tailwind CSS
- ✨ Complete authentication flow (Login/Signup/Password Reset)
- ✨ Deployment-ready configuration files

---

# Problem Statement

Diabetic foot ulcers are one of the most serious complications of diabetes. According to the **International Diabetes Federation**, millions of patients worldwide develop foot ulcers each year, which can lead to infection, hospitalization, and amputation.

Early detection and continuous monitoring are critical.

However, many AI systems behave as **black boxes**, making it difficult for clinicians to trust predictions.

This project focuses on **Explainable AI**, providing both predictions and interpretable outputs that help clinicians understand how the model reaches its decisions.

---

# Features

## 🎯 Core AI Capabilities
* ✅ Diabetic ulcer detection from foot images
* ✅ Integration of clinical data (age, BMI, diabetes duration, etc.)
* ✅ Explainable AI visualizations
* ✅ Grad-CAM heatmaps for image explanation
* ✅ SHAP feature importance for clinical data
* ✅ Patient timeline tracking and ulcer progression monitoring

## 💻 Application Features
* ✅ JWT-based authentication system (Login/Signup/Password Reset)
* ✅ Interactive chatbot workspace with image upload
* ✅ History page with filters (Risk level, search, grid/list view)
* ✅ Real-time AI analysis with confidence scores
* ✅ Modern responsive UI with Tailwind CSS
* ✅ Cloud image storage (Cloudinary)

## 🚀 DevOps & Deployment
* ✅ **5 Health check endpoints** (`/health`, `/health/ping`, `/health/ready`, `/health/live`, `/health/status`)
* ✅ **Render Blueprint** (`render.yaml`) - Auto-deploy backend + frontend + database
* ✅ **Heroku/Railway ready** (`Procfile`)
* ✅ **Docker support** (`docker-compose.yml`)
* ✅ Monitoring with Prometheus and Grafana
* ✅ ML experiment tracking using MLflow
* ✅ System metrics monitoring (CPU, memory, disk)

---

# System Architecture

The system follows a **modular full-stack architecture**.

**Frontend (React)** provides the clinical dashboard interface.

**Backend (FastAPI)** exposes REST APIs for:

* prediction
* authentication
* patient data management
* model inference

The **machine learning pipeline** performs:

* image preprocessing
* prediction
* explainability analysis

High-level architecture:

```
Frontend (React)
        ↓
FastAPI Backend
        ↓
AI Models (PyTorch)
        ↓
Database + Cloud Storage
```

---

# Technology Stack

## Frontend

* React
* Vite
* TailwindCSS
* Chart.js

## Backend

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* Cloudinary (image storage)

## Machine Learning

* PyTorch
* CNN for image classification
* Multimodal model combining image and clinical data
* Grad-CAM visualization
* SHAP explainability

## DevOps / MLOps

* Docker
* Prometheus monitoring
* Grafana dashboards
* MLflow experiment tracking
* DVC dataset versioning

---

# Project Structure

```
diabetic-ulcer-ai-system/

backend/
│
├── app/
│   ├── auth/
│   ├── routes/
│   ├── services/
│   ├── ml/
│   ├── explainability/
│   └── monitoring/
│
└── requirements.txt


frontend/
│
└── src/
    ├── components/
    ├── pages/
    ├── services/
    └── styles/


datasets/
│
├── images/
├── segmentation_masks/
└── clinical_data/


deployment/
│
├── monitoring/
├── nginx/
└── kubernetes/


docs/
```

---

# Getting Started

## 1. Clone the repository

```
git clone https://github.com/chandu1234678/diabetic-ulcer-ai-system.git
cd diabetic-ulcer-ai-system
```

---

# Backend Setup

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run the backend server:

```
uvicorn app.main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```
cd frontend
npm install
npm run dev
```

Frontend will run at:

```
http://localhost:5173
```

---

# Example Workflow

1. User logs into the system
2. Uploads a foot image and clinical information
3. Backend processes the data using the AI model
4. Prediction and explanation are generated
5. Results are displayed in the dashboard

---

# Explainability

This project emphasizes **model interpretability**.

Two main explanation methods are used:

**Grad-CAM**

Highlights important regions of the image used by the model for prediction.

**SHAP**

Shows how clinical features influence the prediction output.

These techniques help clinicians understand **why the system produced a specific prediction**.

---

# Future Improvements

* Improve model accuracy using larger medical datasets
* Train segmentation models for ulcer area detection
* Add longitudinal patient analysis for healing prediction
* Deploy the system to cloud infrastructure
* Develop a mobile interface for field clinics

---

# Learning Outcomes

This project explores several important concepts in modern AI system development:

* Building production-style APIs using FastAPI
* Integrating deep learning models with web applications
* Designing explainable AI systems
* Using Docker for containerized deployments
* Monitoring AI services using Prometheus and Grafana
* Managing ML experiments using MLflow

---

# System Architecture Diagrams

## Overall System Architecture

<img width="4992" height="916" alt="architecture" src="https://github.com/user-attachments/assets/90d6f38f-e2e9-4a13-9440-54bb0631bfbb" />

---

## Prediction Pipeline (AI Workflow)

<img width="1063" height="1683" alt="pipeline" src="https://github.com/user-attachments/assets/fd0fcbcc-1502-47b2-b63a-5ff43791e72a" />

---

## Ulcer Progression Tracking

<img width="1150" height="1345" alt="progression" src="https://github.com/user-attachments/assets/914ba666-da7d-4772-ae9a-0ee1cd22b298" />

---

## Backend API Flow

<img width="2356" height="1266" alt="api-flow" src="https://github.com/user-attachments/assets/d224691b-b6e5-4296-a2a5-c5fcff5f74e6" />

---

---

# 🏥 Health Check Endpoints (Production Ready)

The backend includes **5 health check endpoints** to keep your application alive on free-tier hosting:

| Endpoint | Purpose |
|----------|---------|
| `GET /health` | Main health check - used by Render, Heroku |
| `GET /health/ping` | Simple uptime ping - for monitoring services |
| `GET /health/ready` | Readiness probe - Kubernetes compatible |
| `GET /health/live` | Liveness probe - container orchestration |
| `GET /health/status` | System metrics - CPU, memory, disk usage |

**Prevent Sleeping on Render (Free Tier):**
1. Sign up for free [UptimeRobot](https://uptimerobot.com) account
2. Add HTTP monitor for: `https://your-app.onrender.com/health/ping`
3. Set interval to 5-14 minutes
4. Your app stays awake! 🎉

---

# 🌐 Deployment Guide

## Deploy to Render (Recommended)

**Step 1: Push to GitHub**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

**Step 2: Deploy with Blueprint**
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **New** → **Blueprint**
3. Connect your GitHub repository
4. Render auto-deploys using `render.yaml`:
   - Backend API (Python/FastAPI)
   - Frontend (Static Site)
   - PostgreSQL Database

**Step 3: Configure Environment Variables**
Generate secure keys:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Set in Render dashboard:
- `SECRET_KEY` - Generated secure key
- `JWT_SECRET_KEY` - Another generated key
- `ENVIRONMENT` - `production`
- `CORS_ORIGINS` - Your frontend URL

**Step 4: Set Up Monitoring**
- Create [UptimeRobot](https://uptimerobot.com) account (free)
- Monitor `/health/ping` endpoint
- Prevents app from sleeping!

**📖 Complete Guide:** See [DEPLOYMENT.md](DEPLOYMENT.md) for full instructions including Heroku, Railway, Vercel, Docker.

---

# 📊 Current Application Status

✅ **Backend Server:** Running on port 8000  
✅ **Frontend Server:** Running on port 5173  
✅ **Health Endpoints:** Configured and tested  
✅ **Deployment Files:** render.yaml, Procfile, .env templates  
✅ **Documentation:** DEPLOYMENT.md, APPLICATION_STATUS.md

**Test Locally:**
```bash
# Test health endpoints
curl http://localhost:8000/health
curl http://localhost:8000/health/ping
curl http://localhost:8000/health/status

# Open application
http://localhost:5173
```

**API Documentation:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

# 📁 New Files Added

**Deployment Configuration:**
- `render.yaml` - Render Blueprint (backend + frontend + database)
- `Procfile` - Heroku/Railway deployment
- `DEPLOYMENT.md` - Complete deployment guide
- `APPLICATION_STATUS.md` - Current system status

**Environment Templates:**
- `backend/.env.example` - Backend environment variables template
- `frontend/.env.example` - Frontend environment variables template
- `backend/.env` - Local development configuration (created)
- `frontend/.env` - Frontend API URL configuration (created)

**Enhanced Backend:**
- `backend/app/routes/health.py` - 5 health check endpoints
- `backend/requirements.txt` - Added `psutil` for system monitoring

**New Frontend Pages:**
- `frontend/src/pages/History.jsx` - Interactive history with filters

---

# License

This project is intended for **educational and research purposes only**.

---

<div align="center">

**🎉 Ready to Deploy! Both servers are running. Follow DEPLOYMENT.md to go live.**

**Built with ❤️ for better healthcare**

</div>


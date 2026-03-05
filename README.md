# Diabetic Ulcer Explainable AI Platform

## Overview

This project explores how artificial intelligence can support clinicians in detecting and monitoring diabetic foot ulcers. The goal is to build an **Explainable AI Clinical Decision Support System** that combines image analysis and clinical data to estimate ulcer risk and provide interpretable insights.

The system is designed as a **full-stack AI application** consisting of a React frontend, a FastAPI backend, and a machine learning pipeline. In addition to predictions, the system also generates explanations such as Grad-CAM heatmaps and feature importance visualizations.

The project was built as a learning experience to explore modern technologies including **FastAPI, PyTorch, React, Docker, MLflow, and Prometheus monitoring**.

---

## Problem Statement

Diabetic foot ulcers are one of the most serious complications of diabetes. Early detection and monitoring can help prevent infections, amputations, and long-term complications.

However, many AI systems behave like a “black box”. Clinicians often need explanations to trust model predictions. This project focuses on **Explainable AI**, providing both predictions and interpretable outputs that highlight what the model is learning.

---

## Features

* Diabetic ulcer detection from foot images
* Integration of clinical data (age, BMI, diabetes duration, etc.)
* Explainable AI visualizations
* Grad-CAM heatmaps for image explanation
* SHAP feature importance for clinical data
* Patient timeline tracking and ulcer progression monitoring
* JWT-based authentication system
* Cloud image storage
* Monitoring with Prometheus and Grafana
* ML experiment tracking using MLflow

---

## System Architecture

The system follows a modular full-stack architecture.

Frontend (React) provides the clinical dashboard interface.
Backend (FastAPI) exposes REST APIs for prediction, authentication, and data management.
The ML pipeline performs inference and explainability analysis.

High-level architecture:

Frontend → FastAPI Backend → AI Models → Database

---

## Technology Stack

### Frontend

* React
* Vite
* TailwindCSS
* Chart.js

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication
* Cloudinary (image storage)

### Machine Learning

* PyTorch
* CNN for image classification
* Multimodal model combining image and clinical data
* Grad-CAM visualization
* SHAP explainability

### DevOps / MLOps

* Docker
* Prometheus monitoring
* Grafana dashboards
* MLflow experiment tracking
* DVC dataset versioning

---

## Project Structure

```
hackathon/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── ml/
│   │   ├── explainability/
│   │   └── monitoring/
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── styles/
│
├── datasets/
│   ├── images/
│   ├── segmentation_masks/
│   └── clinical_data/
│
├── deployment/
│   ├── monitoring/
│   ├── nginx/
│   └── kubernetes/
│
└── docs/
```

---

## Getting Started

### 1. Clone the repository

```
git clone https://github.com/yourusername/diabetic-ulcer-ai-system.git
cd diabetic-ulcer-ai-system
```

### 2. Backend Setup

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

### 3. Frontend Setup

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

## Example Workflow

1. User logs into the system
2. Uploads a foot image and clinical information
3. Backend processes the data using the AI model
4. Prediction and explanation are generated
5. Results are displayed in the dashboard

---

## Explainability

The project emphasizes interpretability.

Grad-CAM highlights important image regions used for prediction.

SHAP visualizations show which clinical features influence the model output.

This helps clinicians understand **why the system made a prediction** rather than only providing a result.

---

## Future Improvements

* Improve model accuracy using larger datasets
* Train segmentation models for ulcer area detection
* Add longitudinal patient analysis for healing prediction
* Deploy the system to a cloud environment
* Add mobile support for field clinics

---

## Learning Outcomes

Through this project I explored several modern technologies and concepts:

* Building production-style APIs using FastAPI
* Integrating deep learning models with web applications
* Designing explainable AI systems
* Working with Docker and monitoring tools
* Managing ML experiments using MLflow

This project helped me better understand how AI systems can be built end-to-end and deployed as real applications.

---
## Overall System Architecture

<img width="4992" height="916" alt="mermaid-diagram (11)" src="https://github.com/user-attachments/assets/90d6f38f-e2e9-4a13-9440-54bb0631bfbb" />

## Prediction Pipeline (AI Workflow)

<img width="1063" height="1683" alt="mermaid-diagram (12)" src="https://github.com/user-attachments/assets/fd0fcbcc-1502-47b2-b63a-5ff43791e72a" />

## Ulcer Progression Tracking (Unique Feature)

<img width="1150" height="1345" alt="mermaid-diagram (13)" src="https://github.com/user-attachments/assets/914ba666-da7d-4772-ae9a-0ee1cd22b298" />

## Backend API Flow
<img width="2356" height="1266" alt="mermaid-diagram (14)" src="https://github.com/user-attachments/assets/d224691b-b6e5-4296-a2a5-c5fcff5f74e6" />


## License

This project is intended for educational and research purposes.

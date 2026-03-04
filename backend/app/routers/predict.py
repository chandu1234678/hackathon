from fastapi import APIRouter
from app.schemas.predict_schema import PredictionRequest, PredictionResponse
from app.services.ml_service import run_prediction

router = APIRouter(prefix="/api")

@router.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionRequest):

    prediction, confidence = run_prediction(data.text)

    return PredictionResponse(
        prediction=prediction,
        confidence=confidence
    )
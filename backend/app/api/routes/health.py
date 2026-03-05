from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
	return {"status": "ok", "service": "diabetic-ulcer-ai-system"}

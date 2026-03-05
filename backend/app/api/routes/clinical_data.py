from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/clinical-data/example")
async def get_clinical_data_example() -> dict[str, object]:
	return {
		"patient_id": "sample-001",
		"age": 61,
		"diabetes_type": "type_2",
		"wound_duration_days": 18,
		"infection_signs": True,
	}

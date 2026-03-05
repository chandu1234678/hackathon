def generate_prediction_report(
	prediction: int,
	confidence: float,
	explanation: str,
) -> dict[str, float | int | str]:
	return {
		"prediction": prediction,
		"confidence": confidence,
		"explanation": explanation,
	}

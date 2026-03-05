def run_prediction(text: str) -> tuple[int, float]:
    length_feature = len(text.strip())

    if length_feature >= 20:
        prediction = 1
    else:
        prediction = 0

    confidence = min(0.99, 0.55 + (length_feature / 100.0))
    return prediction, round(confidence, 2)
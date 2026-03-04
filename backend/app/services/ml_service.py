import numpy as np

def run_prediction(text: str):

    # simple demo feature
    length = len(text)

    if length > 10:
        prediction = 1
        confidence = 0.85
    else:
        prediction = 0
        confidence = 0.60

    return prediction, confidence
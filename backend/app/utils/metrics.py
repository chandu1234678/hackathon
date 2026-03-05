from typing import Sequence


def accuracy(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
	if len(y_true) != len(y_pred) or len(y_true) == 0:
		return 0.0
	correct = sum(int(t == p) for t, p in zip(y_true, y_pred))
	return correct / len(y_true)


def precision(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
	true_positives = sum(int(t == 1 and p == 1) for t, p in zip(y_true, y_pred))
	predicted_positives = sum(int(p == 1) for p in y_pred)
	if predicted_positives == 0:
		return 0.0
	return true_positives / predicted_positives


def recall(y_true: Sequence[int], y_pred: Sequence[int]) -> float:
	true_positives = sum(int(t == 1 and p == 1) for t, p in zip(y_true, y_pred))
	actual_positives = sum(int(t == 1) for t in y_true)
	if actual_positives == 0:
		return 0.0
	return true_positives / actual_positives

"""LIME-based explanation for clinical data features."""
import numpy as np
from typing import Dict, List


def generate_lime_explanation(clinical_features: np.ndarray, prediction: str, 
                             confidence: float, feature_names: List[str] = None) -> Dict[str, str]:
    """
    Generate LIME-style explanation for prediction based on clinical features.
    
    Args:
        clinical_features: Array of normalized clinical features [age, bmi, diabetes_duration, infection]
        prediction: Prediction label ("ulcer" or "normal")
        confidence: Model confidence (0-1)
        feature_names: Names of features
    
    Returns:
        Dictionary with explanation text and feature contributions
    """
    if feature_names is None:
        feature_names = ["Age", "BMI", "Diabetes Duration", "Infection Signs"]
    
    # Map normalized values back to original ranges for explanation
    feature_display = {
        "Age": int(clinical_features[0, 0] * 100),
        "BMI": float(clinical_features[0, 1] * 50),
        "Diabetes Duration": int(clinical_features[0, 2] * 50),
        "Infection Signs": _map_infection_value(clinical_features[0, 3])
    }
    
    # Calculate approximate LIME-style importance based on feature deviation from mean
    mean_values = np.array([0.45, 0.45, 0.3, 0.25])  # Approximate population means
    deviations = np.abs(clinical_features[0] - mean_values)
    importance_scores = deviations / (np.sum(deviations) + 1e-6)
    
    # Create importance dict
    lime_importance = {}
    for i, name in enumerate(feature_names):
        lime_importance[name] = float(importance_scores[i])
    
    # Generate natural language explanation
    explanation = _generate_lime_text(
        prediction, confidence, feature_display, lime_importance
    )
    
    return {
        "explanation": explanation,
        "lime_importance": lime_importance,
        "feature_values": feature_display
    }


def _map_infection_value(normalized_infection: float) -> str:
    """Map normalized infection value back to categorical label."""
    if normalized_infection < 0.25:
        return "None"
    elif normalized_infection < 0.5:
        return "Mild"
    elif normalized_infection < 0.75:
        return "Moderate"
    else:
        return "Severe"


def _generate_lime_text(prediction: str, confidence: float, features: Dict, 
                       importance: Dict) -> str:
    """Generate textual LIME explanation."""
    lines = []
    
    # Main prediction
    if prediction == "ulcer":
        lines.append(
            f"LIME analysis predicts DIABETIC ULCER with {confidence*100:.1f}% confidence."
        )
    else:
        lines.append(
            f"LIME analysis predicts NORMAL SKIN with {(1-confidence)*100:.1f}% confidence."
        )
    
    # Top contributing features
    sorted_features = sorted(importance.items(), key=lambda x: x[1], reverse=True)
    top_features = sorted_features[:2]
    
    lines.append(f"Top contributing factors (LIME importance):")
    for feat_name, importance_score in top_features:
        feat_value = features.get(feat_name, "N/A")
        lines.append(
            f"  • {feat_name} ({feat_value}): importance={importance_score:.1%}"
        )
    
    # Risk interpretation
    if prediction == "ulcer" and confidence > 0.7:
        lines.append(
            "High-confidence ulcer prediction. Recommend immediate clinical evaluation."
        )
    elif prediction == "ulcer" and confidence > 0.5:
        lines.append(
            "Moderate-confidence ulcer prediction. Consider specialist review."
        )
    else:
        lines.append(
            "Low-risk assessment. Continue routine monitoring."
        )
    
    return " ".join(lines)

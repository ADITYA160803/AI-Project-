# model_utils.py
import joblib
import os
import numpy as np

ARTIFACT_DIR = os.path.join(os.path.dirname(__file__), "artifacts")
MODEL_PATH = os.path.join(ARTIFACT_DIR, "best_model.joblib")
VECT_PATH = os.path.join(ARTIFACT_DIR, "tfidf.joblib")

def load_artifacts():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECT_PATH):
        raise FileNotFoundError("Model or vectorizer not found in artifacts/. Run training & save artifacts.")
    model = joblib.load(MODEL_PATH)
    vect = joblib.load(VECT_PATH)
    return model, vect

def predict_text(text, model, vect):
    """
    text: str
    returns: dict with label (0 ham, 1 spam), label_name and probability (if available)
    """
    X = vect.transform([text])
    label = int(model.predict(X)[0])
    # attempt to get probabilities (not available for LinearSVC)
    prob = None
    if hasattr(model, "predict_proba"):
        prob = float(model.predict_proba(X)[0].max())
    else:
        # try decision_function then convert to pseudo probability (optional)
        if hasattr(model, "decision_function"):
            try:
                score = model.decision_function(X)[0]
                # Convert using sigmoid for rough probability estimate
                prob = 1.0 / (1.0 + np.exp(-score))
                prob = float(prob if prob >= 0 else 0.0)
            except Exception:
                prob = None

    return {
        "label": label,
        "label_name": "spam" if label == 1 else "safe",
        "score": prob
    }

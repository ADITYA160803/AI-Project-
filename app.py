# app.py
from flask import Flask, request, render_template, jsonify
from model_utils import load_artifacts, predict_text

app = Flask(__name__)

# Load once on startup
model, vect = load_artifacts()

@app.route("/", methods=["GET"
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # form-based prediction (from the web page)
    message = request.form.get("message")
    if not message:
        return render_template("result.html", error="Please enter a message to classify.")
    res = predict_text(message, model, vect)
    return render_template("result.html", message=message, result=res)

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    Accepts JSON: {"message": "text here"}
    Returns JSON: {"label": 0 or 1, "label_name": "ham"|"spam", "score": float|null}
    """
    data = request.get_json(force=True, silent=True)
    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' in JSON body"}), 400
    message = data["message"]
    res = predict_text(message, model, vect)
    return jsonify(res), 200

if __name__ == "__main__":
    # production servers use gunicorn or similar
    app.run(host="0.0.0.0", port=5000, debug=True)

from pathlib import Path
import math

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"

model = joblib.load(MODEL_PATH)

FEATURE_COLUMNS = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course",
    "reading score",
    "writing score",
]


@app.route("/")
def home():
    return render_template("formulario.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True) or request.form

        student_data = {
            "gender": data.get("gender"),
            "race/ethnicity": data.get("race_ethnicity"),
            "parental level of education": data.get("parental_level_of_education"),
            "lunch": data.get("lunch"),
            "test preparation course": data.get("test_preparation_course"),
            "reading score": float(data.get("reading_score")),
            "writing score": float(data.get("writing_score")),
        }

        input_df = pd.DataFrame([student_data], columns=FEATURE_COLUMNS)
        prediction = float(model.predict(input_df)[0])
        rounded_prediction = math.floor(prediction + 0.5)

        return jsonify(
            {
                "math_score": rounded_prediction,
                "mensaje": f"Calificación estimada en matemáticas: {rounded_prediction}",
            }
        )
    except Exception as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(debug=True)

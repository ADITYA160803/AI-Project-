📧 AI/ML Project – Spam Email Detection

This project focuses on detecting spam emails/messages using Machine Learning (ML) and Deep Learning (DL) techniques.
The goal is to classify messages as Spam or Safe (Ham) based on textual features.

📌 Project Overview

Analyze and preprocess email text data

Build multiple ML models:

Naive Bayes

Logistic Regression

Linear SVM

Build Deep Learning models:

ANN (Artificial Neural Network)

CNN (Convolutional Neural Network)

Compare all models and save the best one

Build a Flask-based web application for real-time spam detection

Store trained models using Joblib (pickle)

📁 Files Included
File / Folder	Description
app.py	Main Flask web application
model_utils.py	Loads model, TF-IDF, and performs predictions
requirements.txt	List of dependencies
artifacts/	Contains saved model & TF-IDF vectorizer (best_model.joblib, tfidf.joblib)
templates/	HTML pages (index.html, result.html)
static/	CSS/JS files for UI
README.md	Project documentation
📊 Dataset Information

The dataset used contains:

Labeled email messages

Two classes:

ham → Safe email

spam → Unwanted or phishing email

Text messages in the Masseges column (typo present in dataset)

Dataset Columns:

Category → ham/spam

Masseges → email/message text

Dataset sourced from public datasets used for educational spam-detection tasks.

🧪 Model Comparison (ML vs ANN vs CNN)

To compare model performance, all models were trained on the same dataset using TF-IDF and Tokenizer embeddings.

Models Used

Multinomial Naive Bayes

Logistic Regression

Linear SVM

ANN (Dense layers on TF-IDF)

CNN (Embedding + Conv1D + GlobalMaxPooling)

✔ Best Performing Classical ML Model

The system automatically selects and saves the best classical ML model as:

artifacts/best_model.joblib

✔ Deep Learning Models

These models were trained and analyzed:

ANN → Performs well on text vector features

CNN → Great for learning sequential patterns in text

🧠 Example Prediction Input
"Congratulations! You have won a free gift voucher. Click the link now."

Prediction Result

Naive Bayes / Logistic Regression / SVM → High probability of spam

ANN → Correctly identifies as spam

CNN → Very high confidence spam detection
✔ Deep learning models understand deeper text patterns.

🛠 Technologies Used

Python

NumPy

Pandas

Scikit-learn

TensorFlow / Keras

Flask

Matplotlib

Jupyter / Google Colab

▶ How to Run This Project
1. Install dependencies
pip install -r requirements.txt

2. Ensure the following files exist in artifacts/:

best_model.joblib

tfidf.joblib

3. Run the Flask application
python app.py

4. Open the web app

Visit:

http://127.0.0.1:5000/


Enter any message → Get prediction: Spam / Safe.

🌐 API Access

Send POST request:

Endpoint:

/api/predict


JSON Body:

{
  "message": "Free entry in a contest! Claim now"
}


Response:

{
  "label": 1,
  "label_name": "spam",
  "score": 0.98
}

📌 Notes

The dataset used for training cannot be included here due to licensing.

Models (joblib files) are included for inference only.

ANN & CNN models can also be integrated into the Flask app if needed.

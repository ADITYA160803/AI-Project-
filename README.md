📧 Spam Email Detection System — AI/ML Project

This project implements a Machine Learning–based Email Spam Detection System using classical ML models as well as Deep Learning models (ANN & CNN).
The system can classify any given email/message as Spam or Not Spam (Safe) with high accuracy and provides a clean Flask-based web interface.

🚀 Project Overview:
The project detects spam emails using a combination of:
✅ TF-IDF Feature Extraction
✅ Classical ML Models
⦁	Naive Bayes
⦁	Logistic Regression
⦁	Linear SVM
✅ Deep Learning Models
⦁	ANN (Dense Neural Network)
⦁	CNN (Embedding + Conv1D)

The best-performing classical model is exported and integrated with a Flask Web App for real-time spam prediction.

📦 Spam Email Detection
│
├── app.py                    # Flask web application
├── model_utils.py            # Loads model + TF-IDF and predicts text
├── spam_email_detection_with_ann_cnn.py   # Training script (ML + ANN + CNN)
│
├── artifacts/
│   ├── best_model.joblib     # Saved best ML model
│   ├── tfidf.joblib          # Saved TF-IDF vectorizer
│
├── templates/
│   ├── index.html            # Professional UI for input
│   └── result.html           # Output page for prediction
│
└── requirements.txt          # Required Python packages


📊 Dataset Information

This project uses the Spam/Ham Email Dataset, commonly available on Kaggle.
Dataset contains:
⦁	Email text content
⦁	Corresponding label → ham (safe) or spam
⦁	~5,000 messages
For this project, the CSV file should be named:spam mail.csv

🤖 Models Used
Classical Machine Learning

1.	Naive Bayes=Fast & simple bayesian classifier
2.	Logistic Regression=Linear binary classification
3.	Linear SVM=High-margin classifier
Deep Learning:

1.	ANN=Dense neural network on TF-IDF features
2.	CNN=Text sequence model using embeddings + Conv1D

🏆 Saved Artifacts
After training, the script automatically saves:
artifacts/best_model.joblib
artifacts/tfidf.joblib



🌐 Flask Web Application
The web app allows the user to:
✔ Enter an email/message
✔ Submit for classification
✔ View the result → Spam or Safe
✔ View confidence score (when available)

The interface is built with:
✔ Clean modern UI
✔ Responsive layout
✔ Simple and fast user experience

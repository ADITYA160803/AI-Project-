# 📧 AI/ML Project – Spam Email Detection

This project focuses on detecting spam emails/messages using Machine Learning (ML) and Deep Learning (DL) techniques.  
The goal is to classify messages as **Spam** or **Safe (Ham)** based on textual features.

---

## 📌 Project Overview

✔ Analyze and preprocess email text data  
✔ Build multiple ML models:  
- Naive Bayes  
- Logistic Regression  
- Linear SVM  

✔ Build Deep Learning models:  
- ANN (Artificial Neural Network)  
- CNN (Convolutional Neural Network)  

✔ Compare all models and save the best one  
✔ Build a Flask-based web application for real-time spam detection  
✔ Store trained models using Joblib (pickle)

---

## 📁 Files Included

| File / Folder | Description |
|--------------|-------------|
| `app.py` | Main Flask web application |
| `model_utils.py` | Loads model + TF-IDF and performs predictions |
| `requirements.txt` | All required dependencies |
| `artifacts/` | Stores saved model & vectorizer (`best_model.joblib`, `tfidf.joblib`) |
| `templates/` | HTML UI files (`index.html`, `result.html`) |
| `static/` | CSS/JS files for styling UI |
| `README.md` | Project documentation |
| `spam mail.csv` | Data Set |

---

## 📊 Dataset Information

The dataset contains:

- Labeled email/message text  
- Two classes:  
  - **ham** → Safe  
  - **spam** → Unwanted / phishing  

Dataset Columns:

- `Category` → ham / spam  
- `Masseges` → message text  

Dataset is publicly available and commonly used for educational spam detection tasks.

---

## 🧪 Model Comparison (ML vs ANN vs CNN)

All models were trained on the same dataset:

### **Models Used**
- Multinomial Naive Bayes  
- Logistic Regression  
- Linear SVM  
- ANN (Dense layers on TF-IDF)  
- CNN (Embedding + Conv1D)

### ✔ Best Classical ML Model Saved:
```
artifacts/best_model.joblib
```

### ✔ Deep Learning Models:
- ANN → Good on vectorized text  
- CNN → Excellent for sequential text features  

---

## 🧠 Example Prediction

**Input:**
```
"Congratulations! You have won a free gift voucher. Click the link now."
```

**Predictions:**
- Classical ML → Spam  
- ANN → Spam  
- CNN → Spam (very high confidence)

---

## 🛠 Technologies Used

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- TensorFlow / Keras  
- Flask  
- Matplotlib  
- Jupyter / Google Colab  

---

## ▶ How to Run This Project

### **1. Install dependencies**
```
pip install -r requirements.txt
```

### **2. Ensure artifacts exist**
Inside the `artifacts/` folder:  
- `best_model.joblib`  
- `tfidf.joblib`

### **3. Run the Flask app**
```
python app.py
```

### **4. Open the Web App**
Visit in browser:
```
http://127.0.0.1:5000/
```

Enter any message → get prediction (Spam / Safe).

---

## 🌐 API Access

### **POST Endpoint**
```
/api/predict
```

### **JSON Body**
```json
{
  "message": "Free entry in a contest! Claim now"
}
```

### **Response**
```json
{
  "label": 1,
  "label_name": "spam",
  "score": 0.98
}
```

---

## 📌 Notes

- Only trained model files are included for prediction.
- ANN & CNN can also be integrated into Flask if required.

---


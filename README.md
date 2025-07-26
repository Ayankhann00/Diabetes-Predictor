# 🩺 Diabetes Prediction Web App

This project is a **machine learning web application** that predicts whether a person is diabetic based on medical inputs. The app is built using **Streamlit** and powered by a **Support Vector Machine (SVM)** model trained on the famous **Pima Indians Diabetes Dataset**.

![streamlit-diabetes](https://img.shields.io/badge/Machine%20Learning-SVM-blue) ![streamlit-badge](https://img.shields.io/badge/Built%20with-Streamlit-orange) ![Python](https://img.shields.io/badge/Python-3.9+-green)

---

## 📊 Demo

https://your-deployed-app-link (Add your Streamlit Cloud or Hugging Face Space URL here)

---

## 📁 Project Structure

├── app.py # Streamlit app
├── svm_model.sav # Trained SVM model (via joblib)
├── scaler.sav # StandardScaler object for input preprocessing
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🚀 Features

- Simple and interactive web UI using **Streamlit**
- Pre-trained **SVM** model with high accuracy
- Input fields for all relevant medical data:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- Displays **instant prediction** as Diabetic or Not Diabetic

---

## 🧠 Model Info

- **Dataset**: Pima Indians Diabetes Dataset (from Kaggle/UCI)
- **Model Used**: Support Vector Machine (SVM)
- **Preprocessing**: `StandardScaler` for input normalization
- **Tools**: `scikit-learn`, `joblib`, `numpy`, `Streamlit`

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app.py
🧪 Sample Test Case

You can try this example to test the app (a diabetic case):

Field	Value
Pregnancies	6
Glucose Level	148
Blood Pressure	72
Skin Thickness	35
Insulin Level	0
BMI	33.6
Diabetes Pedigree Function	0.627
Age	50
✅ Requirements

Python 3.8+
Streamlit
scikit-learn
numpy
joblib
Add this to requirements.txt:

streamlit
scikit-learn
numpy
joblib
![WhatsApp Image 2025-07-27 at 02 06 18](https://github.com/user-attachments/assets/bd7d6df0-6cba-48a7-a278-34a3490e7585)

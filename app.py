import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('svm_model.sav')
scaler = joblib.load('scaler.sav')

st.title("Diabetes Prediction App")
st.write("Enter the patient details to check if they are diabetic.")

# Input fields
pregnancies = st.number_input('Pregnancies', min_value=0)
glucose = st.number_input('Glucose Level', min_value=0)
blood_pressure = st.number_input('Blood Pressure', min_value=0)
skin_thickness = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin Level', min_value=0)
bmi = st.number_input('BMI', min_value=0.0, format="%.1f")
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, format="%.3f")
age = st.number_input('Age', min_value=0)

if st.button("Predict"):
    input_data = (pregnancies, glucose, blood_pressure, skin_thickness,
                  insulin, bmi, dpf, age)
    input_array = np.asarray(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("The person is diabetic.")
    else:
        st.success("The person is not diabetic.")

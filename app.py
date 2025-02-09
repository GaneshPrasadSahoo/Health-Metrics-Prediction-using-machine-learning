import streamlit as st
import pandas as pd
from joblib import load

dt = load('decision_tree_model.joblib')

st.markdown("<h1 style='text-align: center; color: white;'>Health Metrics Prediction</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    gender_input = st.selectbox("Gender", ["Male", "Female"])
    gender = 0 if gender_input == "Male" else 1  # 0 for Male, 1 for Female
    age = st.number_input("Age", min_value=0, max_value=120, value=30)

with col2:
    sleep_duration = st.number_input("Sleep Duration (hours)", min_value=0.0, max_value=24.0, value=7.0)
    physical_activity_level = st.number_input("Physical Activity Level (1-10)", min_value=0, max_value=10, value=5)

with col3:
    daily_steps = st.number_input("Daily Steps", min_value=0, value=5000)
    bmi_category_input = st.selectbox("BMI Category", ["Overweight", "Normal", "Obese", "Normal Weight"])
    bmi_category_map = {"Overweight": 3, "Normal": 0, "Obese": 2, "Normal Weight": 1}
    bmi_category = bmi_category_map[bmi_category_input]  # Map input to numeric value

new_input = pd.DataFrame([[gender, age, sleep_duration, physical_activity_level, daily_steps, bmi_category]],
                         columns=['Gender', 'Age', 'Sleep Duration', 'Physical Activity Level', 'Daily Steps', 'BMI Category'])

def classify_blood_pressure(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Blood Pressure is Normal"
    elif 120 <= systolic <= 129 and diastolic < 80:
        return "Elevated Blood Pressure"
    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "Hypertension Stage 1"
    elif systolic >= 140 or diastolic >= 90:
        if systolic > 180 or diastolic > 120:
            return "Hypertensive Crisis: Emergency Care Needed!"
        return "Hypertension Stage 2"
    return "Uncategorized Blood Pressure"

def classify_stress_level(stress_level):
    if 1 <= stress_level <= 3:
        return "Low Stress"
    elif 4 <= stress_level <= 6:
        return "Moderate Stress"
    elif 7 <= stress_level <= 8:
        return "High Stress"
    return "Uncategorized Stress Level"

if st.button("Predict"):
    prediction = dt.predict(new_input)
    
    systolic, diastolic, stress_level, heart_rate = prediction[0]
    
    blood_pressure_status = classify_blood_pressure(systolic, diastolic)

    stress_status = classify_stress_level(stress_level)

    st.markdown(f"<h2 style='color: lightcyan;'>Predicted Results</h2>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='color: lightgreen;'><strong>Blood Pressure:</strong> {int(systolic)}/{int(diastolic)}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: lightblue;'>Systolic = {int(systolic)}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: lightblue;'>Diastolic = {int(diastolic)}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: orange;'><strong>Blood Pressure Status:</strong> {blood_pressure_status}</p>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='color: lightblue;'><strong>Stress Level:</strong> {int(stress_level)} ({stress_status})</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: lightblue;'><strong>Heart Rate:</strong> {int(heart_rate)}</p>", unsafe_allow_html=True)

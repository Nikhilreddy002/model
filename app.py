# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import joblib

from xgboost import XGBClassifier

#Loading up the classification model we created
xgb=XGBClassifier()

# Model to be loaded
model = joblib.load('xgb_model.joblib')
#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(no_times_pregnant, glucose_concentration, blood_pressure, skin_fold_thickness, serum_insulin, bmi, diabetes_pedigree,age ):
    
    df = pd.DataFrame([[no_times_pregnant, glucose_concentration, blood_pressure, skin_fold_thickness, serum_insulin, bmi, diabetes_pedigree,age]], columns=['no_times_pregnant', 'glucose_concentration', 'blood_pressure', 'skin_fold_thickness','serum_insulin', 'bmi', 'diabetes pedigree','age'])
    prediction = model.predict(df)
    return prediction

st.title('Diabetics Disease Classification')
st.header('Enter the Health Info for the Diabetic Diagnosis:')
no_times_pregnant = st.number_input('no_times_pregnant:', min_value=0, max_value=10, value=1)
glucose_concentration = st.number_input('glucose_concentration:', min_value=10, max_value=1000, value=70)
blood_pressure = st.number_input('blood_pressure:', min_value=20, max_value=500, value=100)
skin_fold_thickness = st.number_input('skin_fold_thickness:', min_value=1, max_value=2000, value=1)
serum_insulin = st.number_input('serum_insulin:', min_value=1, max_value=2000, value=1)
bmi = st.number_input('bmi:', min_value=0.0, max_value=100.0, value=0.1)
diabetes_pedigree = st.number_input('diabetes pedigree:', min_value=0.0, max_value=100.0, value=0.1)
age = st.number_input('age:', min_value=1, max_value=200, value=1)

if st.button('Submit_Diabetics_Infos'):
    diabetics_price = predict(no_times_pregnant, glucose_concentration, blood_pressure, skin_fold_thickness, serum_insulin, bmi, diabetes_pedigree,age )
    st.success(f'The Diabetics Diagnosis : {diabetics_price[0]:.2f}')

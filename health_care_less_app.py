import streamlit as st
import pandas as pd
import joblib
from preprocess import preprocess_input

model = joblib.load('Healthcare_fraud_detection_lessed.pkl')
st.title("Health Care Fraud Detection")
uploaded_file = st.file_uploader("Upload healthcare claim data (CSV)")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Raw input data", data)

    # Preprocess
    processed_data = preprocess_input(data)

    if st.button("Predict Fraud"):
        predictions = model.predict(processed_data)
        st.write("Fraud Predictions:")
        st.write(predictions) 

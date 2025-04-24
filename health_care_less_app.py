import streamlit as st
import pandas as pd
import joblib
from preprocess import preprocess_input

# Load the model
model = joblib.load('Healthcare_fraud_detection_lessed.pkl')

st.title("Health Care Fraud Detection")

# Select input mode
input_mode = st.radio("Select input method", ("Upload CSV file", "Manual input"))

if input_mode == "Upload CSV file":
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

else:
    st.subheader("Enter claim details manually")

    # Example fields (you can customize this based on your actual columns)
    provider = st.text_input("Enter ProviderID")
    beneficiar = st.text_input("Enter BeneficierID")
    amt_reimbursed = st.number_input("Enter claim anount re-imbursed")
    phyID = st.text_input("Enter PhysicianID")
    Gender = st.number_input("Enter Gender(1-Male,2-Female)")
    Race = st.number_input("Enter Race(1-4)")
    State = st.number_input("Enter State number")
    county = st.number_input("Enter county Number")
    ClaimStartDt = st.text_input("Enter ClaimStartDt")
    ClaimEndDt = st.text_input("Enter ClaimEndDt")
    AdmissionDt = st.text_input("Enter AdmissionDt")
    DischargeDt = st.text_input("Enter DischargeDt")
    DOB = st.text_input("Enter DOB")
    RenalDiseaseIndicator = st.text_input("Enter RenalDiseaseIndicator")
    DiagnosisGroupCode = st.text_input("Enter DiagnosisGroupCode")
    DeductibleAmtPaid = st.number_input("Enter DeductibleAmtPaid")
    ClmDiagnosisCode_1 = st.number_input("Enter ClmDiagnosisCode_1")

   # Assemble input into DataFrame
manual_input = pd.DataFrame({
    'Provider': [provider],
    'BeneficiaryID': [beneficiar],
    'Claim_Reimbursed': [amt_reimbursed],
    'PhysicianID': [phyID],
    'Gender': [Gender],
    'Race': [Race],
    'State': [State],
    'County': [county],
    'ClaimStartDt': [ClaimStartDt],
    'ClaimEndDt': [ClaimEndDt],
    'AdmissionDt': [AdmissionDt],
    'DischargeDt': [DischargeDt],
    'DOB': [DOB],
    'Claim_Duration': [claim_duration],
    'RenalDiseaseIndicator': [RenalDiseaseIndicator],
    'DiagnosisGroupCode': [DiagnosisGroupCode],
    'DeductibleAmtPaid': [DeductibleAmtPaid],
    'ClmDiagnosisCode_1': [ClmDiagnosisCode_1]
# default 
    'ChronicCond_Alzheimer': [0],
    'ChronicCond_Heartfailure': [0],
    'ChronicCond_KidneyDisease': [0],
    'ChronicCond_Cancer': [0],
    'ChronicCond_ObstrPulmonary': [0],
    'ChronicCond_Depression': [0],
    'ChronicCond_Diabetes': [0],
    'ChronicCond_IschemicHeart': [0],
    'ChronicCond_Osteoporasis': [0],
    'ChronicCond_rheumatoidarthritis': [0],
    'ChronicCond_stroke': [0],
})

    st.write("Input Summary:", manual_input)

    if st.button("Predict Fraud (Manual)"):
        processed_manual = preprocess_input(manual_input)
        predictions = model.predict(processed_manual)
        st.write("Fraud Prediction:")
        st.write(predictions)

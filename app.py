import streamlit as st
import pickle
import pandas as pd

# Load model
with open('my_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Loan Approval Predictor")

# User inputs
fico = st.number_input("FICO Score", min_value=300, max_value=850)
income = st.number_input("Monthly Income", min_value=0)
loan = st.number_input("Loan Amount", min_value=0)
housing = st.number_input("Monthly Housing Payment", min_value=0)

# Create input dataframe
input_data = pd.DataFrame({
    'FICO_score': [fico],
    'Monthly_Gross_Income': [income],
    'Requested_Loan_Amount': [loan],
    'Monthly_Housing_Payment': [housing]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Denied")

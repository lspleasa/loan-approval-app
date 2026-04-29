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

# ALL model columns
columns = ['Requested_Loan_Amount', 'FICO_score', 'Monthly_Gross_Income',
       'Monthly_Housing_Payment', 'Ever_Bankrupt_or_Foreclose',
       'Reason_credit_card_refinancing', 'Reason_debt_conslidation',
       'Reason_home_improvement', 'Reason_major_purchase', 'Reason_other',
       'Fico_Score_group_fair', 'Fico_Score_group_good',
       'Fico_Score_group_poor', 'Fico_Score_group_very_good',
       'Employment_Status_part_time', 'Employment_Status_unemployed',
       'Employment_Sector_consumer_discretionary',
       'Employment_Sector_consumer_staples', 'Employment_Sector_energy',
       'Employment_Sector_financials', 'Employment_Sector_health_care',
       'Employment_Sector_industrials',
       'Employment_Sector_information_technology',
       'Employment_Sector_materials', 'Employment_Sector_nan',
       'Employment_Sector_real_estate', 'Employment_Sector_utilities',
       'Lender_B', 'Lender_C']

# Create empty input
input_data = pd.DataFrame([[0]*len(columns)], columns=columns)

# Fill user inputs
input_data['FICO_score'] = fico
input_data['Monthly_Gross_Income'] = income
input_data['Requested_Loan_Amount'] = loan
input_data['Monthly_Housing_Payment'] = housing

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Denied")

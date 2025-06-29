import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")


st.set_page_config(page_title="RiskGuard AI: Credit Risk Modelling", page_icon="📊")
st.title("RiskGuard AI: Credit Risk Modelling")


row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

loan_to_income_ratio = loan_amount / income if income > 0 else 0

with row2[0]:
    st.text("Loan to Income Ratio:")
    st.text(f"{loan_to_income_ratio:.2f}")
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=36)
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

if st.button('Calculate Risk'):
    payload = {
        "age": age,
        "income": income,
        "loan_amount": loan_amount,
        "loan_tenure_months": loan_tenure_months,
        "avg_dpd_per_delinquency": avg_dpd_per_delinquency,
        "delinquency_ratio": delinquency_ratio,
        "credit_utilization_ratio": credit_utilization_ratio,
        "num_open_accounts": num_open_accounts,
        "residence_type": residence_type,
        "loan_purpose": loan_purpose,
        "loan_type": loan_type
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Prediction received!")
            st.write(f"**Default Probability:** {result['probability']:.2%}")
            st.write(f"**Credit Score:** {result['credit_score']}")
            st.write(f"**Rating:** {result['rating']}")
        else:
            st.error(f"❌ API error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"❌ Connection error: {e}")

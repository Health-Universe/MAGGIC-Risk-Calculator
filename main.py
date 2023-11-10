import streamlit as st

def calculate_maggic_risk(age, gender, ejection_fraction, nyha_class, systolic_bp, is_diabetic, has_copd, on_beta_blocker):
    # Placeholder coefficients for each factor - these are not real
    coefficients = {
        'age': 0.1, 'gender': 2, 'ejection_fraction': -0.2, 'nyha_class': 3,
        'systolic_bp': -0.1, 'is_diabetic': 4, 'has_copd': 4, 'on_beta_blocker': -3
    }

    # Risk calculation - this is a hypothetical formula
    risk_score = (age * coefficients['age'] + 
                  coefficients['gender'] * (1 if gender == 'Male' else 0) +
                  ejection_fraction * coefficients['ejection_fraction'] +
                  nyha_class * coefficients['nyha_class'] +
                  systolic_bp * coefficients['systolic_bp'] +
                  coefficients['is_diabetic'] * (1 if is_diabetic else 0) +
                  coefficients['has_copd'] * (1 if has_copd else 0) +
                  coefficients['on_beta_blocker'] * (1 if on_beta_blocker else 0))

    return risk_score


st.title("MAGGIC Risk Calculator for Heart Failure")

# User inputs
age = st.number_input("Age", min_value=0, max_value=120, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
ejection_fraction = st.number_input("Ejection Fraction (%)", min_value=0, max_value=100, value=55)
nyha_class = st.number_input("NYHA Class (1-4)", min_value=1, max_value=4, value=2)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=0, max_value=200, value=120)
is_diabetic = st.checkbox("Diabetic")
has_copd = st.checkbox("COPD")
on_beta_blocker = st.checkbox("On Beta Blocker")

if st.button("Calculate Risk"):
    risk_score = calculate_maggic_risk(age, gender, ejection_fraction, nyha_class, systolic_bp, is_diabetic, has_copd, on_beta_blocker)
    st.write("Your MAGGIC Risk Score is:", risk_score)


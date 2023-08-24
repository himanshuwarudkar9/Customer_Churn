import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('Trained_model.pkl', 'rb'))

# Define function to preprocess input data
def preprocess_input(age, gender, location, subscription_length, monthly_bill, total_usage):
    data = [[age, gender, location, subscription_length, monthly_bill, total_usage]]
    return data

# Define function to predict churn
def predict_churn(data):
    prediction = model.predict(data)
    return prediction

def main():   
    st.title("Customer Churn Prediction")

    # Add a picture or logo
    st.image('https://www.scnsoft.com/blog-pictures/business-intelligence/customer-churn-analysis.png', width=200)

    age = st.number_input("Age", min_value=0, step=1)
    gender = st.radio("Gender", ['Male', 'Female'])
    location = st.selectbox("Location", ['Houston', 'Los Angeles', 'Miami', 'Chicago', 'New York'])
    subscription_length = st.number_input("Subscription Length (Months)", min_value=0, step=1)
    monthly_bill = st.number_input("Monthly Bill", min_value=0.0, step=0.1)
    total_usage = st.number_input("Total Usage (GB)", min_value=0.0, step=0.1)
    
    if st.button("Predict Churn"):
        gender_encoded = 1 if gender == "Male" else 0
        data = preprocess_input(age, gender_encoded, location, subscription_length, monthly_bill, total_usage)

        prediction = predict_churn(data)

        if prediction[0] == 1:
            result = "likely to churn."
        else:
            result = "not likely to churn."

        st.success(f"This customer is {result}")

if __name__ == "__main__":
    main()

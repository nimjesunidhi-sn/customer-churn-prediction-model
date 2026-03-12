import streamlit as st
import pandas as pd
import pickle

# load model
model = pickle.load(open("churn_model.pkl","rb"))

st.title("Customer Churn Prediction")

st.header("Enter Customer Details")

# numeric inputs
tenure = st.number_input("Tenure Months",0,100)
MonthlyCharges = st.number_input("Monthly Charges")
TotalCharges = st.number_input("Total Charges")

# categorical inputs
Gender = st.selectbox("Gender",["Female","Male"])
SeniorCitizen = st.selectbox("Senior Citizen",[0,1])
Partner = st.selectbox("Partner",["No","Yes"])
Dependents = st.selectbox("Dependents",["No","Yes"])
PhoneService = st.selectbox("Phone Service",["No","Yes"])
MultipleLines = st.selectbox("Multiple Lines",["No","Yes"])
InternetService = st.selectbox("Internet Service",["DSL","Fiber optic","No"])
OnlineSecurity = st.selectbox("Online Security",["No","Yes"])
OnlineBackup = st.selectbox("Online Backup",["No","Yes"])
DeviceProtection = st.selectbox("Device Protection",["No","Yes"])
TechSupport = st.selectbox("Tech Support",["No","Yes"])
StreamingTV = st.selectbox("Streaming TV",["No","Yes"])
StreamingMovies = st.selectbox("Streaming Movies",["No","Yes"])
Contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
PaperlessBilling = st.selectbox("Paperless Billing",["No","Yes"])
PaymentMethod = st.selectbox("Payment Method",
["Electronic check","Mailed check","Bank transfer","Credit card"])

# predict button
if st.button("Predict Churn"):

    data = pd.DataFrame({
        "tenure":[tenure],
        "MonthlyCharges":[MonthlyCharges],
        "TotalCharges":[TotalCharges],
        "Gender":[Gender],
        "SeniorCitizen":[SeniorCitizen],
        "Partner":[Partner],
        "Dependents":[Dependents],
        "PhoneService":[PhoneService],
        "MultipleLines":[MultipleLines],
        "InternetService":[InternetService],
        "OnlineSecurity":[OnlineSecurity],
        "OnlineBackup":[OnlineBackup],
        "DeviceProtection":[DeviceProtection],
        "TechSupport":[TechSupport],
        "StreamingTV":[StreamingTV],
        "StreamingMovies":[StreamingMovies],
        "Contract":[Contract],
        "PaperlessBilling":[PaperlessBilling],
        "PaymentMethod":[PaymentMethod]
    })

    # convert text → numeric

    data["Gender"] = data["Gender"].map({"Female":0,"Male":1})
    data["Partner"] = data["Partner"].map({"No":0,"Yes":1})
    data["Dependents"] = data["Dependents"].map({"No":0,"Yes":1})
    data["PhoneService"] = data["PhoneService"].map({"No":0,"Yes":1})
    data["MultipleLines"] = data["MultipleLines"].map({"No":0,"Yes":1})
    data["OnlineSecurity"] = data["OnlineSecurity"].map({"No":0,"Yes":1})
    data["OnlineBackup"] = data["OnlineBackup"].map({"No":0,"Yes":1})
    data["DeviceProtection"] = data["DeviceProtection"].map({"No":0,"Yes":1})
    data["TechSupport"] = data["TechSupport"].map({"No":0,"Yes":1})
    data["StreamingTV"] = data["StreamingTV"].map({"No":0,"Yes":1})
    data["StreamingMovies"] = data["StreamingMovies"].map({"No":0,"Yes":1})
    data["PaperlessBilling"] = data["PaperlessBilling"].map({"No":0,"Yes":1})

    data["Contract"] = data["Contract"].map({
        "Month-to-month":0,
        "One year":1,
        "Two year":2
    })

    data["InternetService"] = data["InternetService"].map({
        "DSL":0,
        "Fiber optic":1,
        "No":2
    })

    data["PaymentMethod"] = data["PaymentMethod"].map({
        "Electronic check":0,
        "Mailed check":1,
        "Bank transfer":2,
        "Credit card":3
    })

    # prediction
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer will stay")
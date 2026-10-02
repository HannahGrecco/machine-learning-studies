import streamlit as st
import json
import requests

st.set_page_config(
    page_title="Sales Revenue Prediction",
    page_icon="📈",
    layout="centered"
)

st.title("Sales Revenue Prediction")
st.write(
    "Enter the salesperson's information below to estimate the expected revenue."
)

st.divider()

experience_time = st.slider(
    "Experience Time (months)",
    min_value=1,
    max_value=120,
    value=60,
    step=1
)

sales_count = st.slider(
    "Sales Count",
    min_value=10,
    max_value=100,
    value=50,
    step=1
)

seasonal_factor = st.slider(
    "Seasonal Factor",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

st.divider()

if st.button("Predict Revenue", use_container_width=True):

    payload = {
        "experience_time": experience_time,
        "sales_count": sales_count,
        "seasonal_factor": seasonal_factor
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        if response.status_code == 200:

            prediction = response.json()

            revenue = prediction["predicted_revenue"]

            st.success("Prediction completed successfully!")

            st.metric(
                label="Predicted Revenue",
                value=f"R$ {revenue:,.2f}"
            )

        else:
            st.error("The API returned an error.")

    except requests.exceptions.ConnectionError:
        st.error("Unable to connect to the FastAPI server.")
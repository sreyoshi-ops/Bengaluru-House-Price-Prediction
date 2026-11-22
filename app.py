
import streamlit as st
import pandas as pd
import joblib

# Page configuration

st.set_page_config(
    page_title="Bengaluru House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Load trained model

data = joblib.load("house_price_model.pkl")

model = data['model']

locations = data['locations']

area_types = data['area_types']

# Application title

st.title("🏠 Bengaluru House Price Prediction")

st.write(
    "Predict house prices in Bengaluru using Machine Learning."
)

st.divider()

# User inputs

st.subheader("Enter Property Details")

area_type = st.selectbox(
    "Area Type",
    area_types
)

location = st.selectbox(
    "Location",
    locations
)

total_sqft = st.number_input(
    "Total Square Feet",
    min_value=300.0,
    max_value=50000.0,
    value=1200.0
)

bhk = st.selectbox(
    "Number of Bedrooms (BHK)",
    [1, 2, 3, 4, 5, 6, 7, 8]
)

bath = st.selectbox(
    "Number of Bathrooms",
    [1, 2, 3, 4, 5, 6, 7, 8]
)

balcony = st.selectbox(
    "Number of Balconies",
    [0, 1, 2, 3, 4]
)

# Prediction button

if st.button("Predict House Price", use_container_width=True):

    if total_sqft / bhk < 300:
        st.warning(
            "The selected area is unusually small for this BHK configuration."
        )

    elif bath > bhk + 2:
        st.warning(
            "Please enter a realistic bathroom count."
        )

    else:

        input_data = pd.DataFrame({

            'area_type': [area_type],

            'location': [location],

            'total_sqft': [total_sqft],

            'bhk': [bhk],

            'bath': [bath],

            'balcony': [balcony]

        })

        prediction = model.predict(input_data)[0]

        st.success("Prediction completed!")

        st.metric(
            label="Estimated House Price",
            value=f"₹ {prediction:.2f} Lakhs"
        )

        st.write(
            f"Approximately ₹ {prediction * 100000:,.0f}"
        )

st.divider()

st.caption(
    "Developed using Python, Pandas, Scikit-learn and Streamlit."
)

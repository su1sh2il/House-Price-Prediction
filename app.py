import streamlit as st
import pandas as pd
import joblib

model = joblib.load("gb_model.pkl")

st.title("🏠 House Price Prediction")

lot_area = st.number_input("Lot Area")

house_style = st.selectbox(
    "House Style",
    ["1Story", "2Story", "1.5Fin", "1.5Unf", "SFoyer", "SLvl"]
)

neighborhood = st.text_input("Neighborhood")

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2000
)

overall_qual = st.slider(
    "Overall Quality",
    1, 10, 5
)

total_bsmt_sf = st.number_input(
    "Total Basement Area"
)

garage_cars = st.number_input(
    "Garage Capacity",
    min_value=0,
    max_value=10,
    value=2
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "LotArea": [lot_area],
        "HouseStyle": [house_style],
        "Neighborhood": [neighborhood],
        "YearBuilt": [year_built],
        "OverallQual": [overall_qual],
        "TotalBsmtSF": [total_bsmt_sf],
        "GarageCars": [garage_cars]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ${prediction[0]:,.2f}"
    )
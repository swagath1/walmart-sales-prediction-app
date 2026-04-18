import streamlit as st
import pickle
import pandas as pd

# Load model and columns
model = pickle.load(open("wallmart_sales.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("🛒 Walmart Sales Prediction")

st.write("Enter details to predict weekly sales")


temp = st.number_input("Temperature")
fuel = st.number_input("Fuel Price")
month = st.number_input("Month (1-12)", min_value=1, max_value=12)
week = st.number_input("Week (1-52)", min_value=1, max_value=52)
holiday = st.selectbox("Is Holiday", [0, 1])
type_input = st.selectbox("Store Type", ["A", "B", "C"])


if st.button("Predict Sales"):

    # Create empty input dict with all columns
    input_dict = {col: 0 for col in columns}

    # Fill user inputs
    if "Temperature" in input_dict:
        input_dict["Temperature"] = temp

    if "Fuel_Price" in input_dict:
        input_dict["Fuel_Price"] = fuel

    if "Month" in input_dict:
        input_dict["Month"] = month

    if "Week" in input_dict:
        input_dict["Week"] = week

    if "IsHoliday" in input_dict:
        input_dict["IsHoliday"] = holiday

    # Handle Type (get_dummies)
    if type_input == "A" and "Type_A" in input_dict:
        input_dict["Type_A"] = 1
    elif type_input == "B" and "Type_B" in input_dict:
        input_dict["Type_B"] = 1
    elif type_input == "C" and "Type_C" in input_dict:
        input_dict["Type_C"] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Prediction
    prediction = model.predict(input_df)

    st.success(f"💰 Predicted Weekly Sales: {prediction[0]:,.2f}")

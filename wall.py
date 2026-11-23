import os
import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Walmart Sales Prediction", page_icon="🛒", layout="centered")
st.title("🛒 Walmart Weekly Sales Prediction")
st.markdown("Enter the feature values below to estimate **Weekly Sales**.")

from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parent


@st.cache_resource
def load_artifacts():
    candidate_models = [
        BASE_DIR / "wallmart_sales.pkl",
        BASE_DIR / "walmart_sales.pkl",
        BASE_DIR / "model.pkl",
    ]
    model_path = next((p for p in candidate_models if p.exists()), None)
    cols_path = BASE_DIR / "columns.pkl"

    if model_path is None or not cols_path.exists():
        files_in_dir = sorted(p.name for p in BASE_DIR.iterdir())
        raise FileNotFoundError(
            f"Missing model or columns.pkl in {BASE_DIR}. "
            f"Found files: {files_in_dir}. "
            "Make sure both .pkl files are pushed to your GitHub repo."
        )

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(cols_path, "rb") as f:
        columns = pickle.load(f)

    return model, columns


model, columns = load_artifacts()

col1, col2 = st.columns(2)

with col1:
    store = st.number_input("Store", min_value=1, max_value=45, value=1, step=1)
    dept = st.number_input("Dept", min_value=1, max_value=99, value=1, step=1)
    year = st.number_input("Year", min_value=2010, max_value=2030, value=2012, step=1)
    month = st.number_input("Month", min_value=1, max_value=12, value=11, step=1)
    week = st.number_input("Week", min_value=1, max_value=53, value=45, step=1)
    is_holiday = st.selectbox("IsHoliday", options=[0, 1], index=0)

with col2:
    store_type = st.selectbox("Store Type", options=["A", "B", "C"], index=0)
    size = st.number_input("Size", min_value=0.0, value=151315.0, step=1000.0)
    temperature = st.number_input("Temperature", value=60.0)
    fuel_price = st.number_input("Fuel_Price", min_value=0.0, value=3.50, format="%.3f")
    cpi = st.number_input("CPI", min_value=0.0, value=175.0)
    unemployment = st.number_input("Unemployment", min_value=0.0, value=7.5)

with st.expander("Optional MarkDown Values (Leave as 0 if none)"):
    md1 = st.number_input("MarkDown1", value=0.0)
    md2 = st.number_input("MarkDown2", value=0.0)
    md3 = st.number_input("MarkDown3", value=0.0)
    md4 = st.number_input("MarkDown4", value=0.0)
    md5 = st.number_input("MarkDown5", value=0.0)

if st.button("Predict Weekly Sales", type="primary", use_container_width=True):
    row = {col: 0 for col in columns}

    values = {
        "Store": store,
        "Dept": dept,
        "Year": year,
        "Month": month,
        "Week": week,
        "IsHoliday": is_holiday,
        "Size": size,
        "Temperature": temperature,
        "Fuel_Price": fuel_price,
        "CPI": cpi,
        "Unemployment": unemployment,
        "MarkDown1": md1,
        "MarkDown2": md2,
        "MarkDown3": md3,
        "MarkDown4": md4,
        "MarkDown5": md5,
    }

    for k, v in values.items():
        if k in row:
            row[k] = v

    type_col = f"Type_{store_type}"
    if type_col in row:
        row[type_col] = 1

    input_df = pd.DataFrame([row]).reindex(columns=columns, fill_value=0)
    prediction = model.predict(input_df)[0]

    st.success(f"### Predicted Weekly Sales: ${prediction:,.2f}")

import streamlit as st
import pandas as pd

st.title("📈 Traffic Analytics")

st.write("Upload same dataset again to analyze distributions.")

uploaded_file = st.file_uploader("Upload CSV for Analytics", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    numeric_data = data.select_dtypes(include=["number"])

    if numeric_data.shape[1] == 0:
        st.error("No numeric features found.")
    else:
        st.subheader("Feature Distributions")
        for column in numeric_data.columns:
            st.write(f"Distribution of {column}")
            st.bar_chart(numeric_data[column])
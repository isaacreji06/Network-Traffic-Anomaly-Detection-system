import streamlit as st
import pandas as pd
from model import run_anomaly_detection

st.title("📊 Upload & Detect Network Anomalies")

uploaded_file = st.file_uploader("Upload Network Traffic CSV", type=["csv"])

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    processed_data, model = run_anomaly_detection(data)

    if processed_data is None:
        st.error("No numeric features found.")
    else:
        total_rows = len(processed_data)
        anomaly_count = (processed_data["anomaly"] == "Anomalous").sum()
        anomaly_percentage = (anomaly_count / total_rows) * 100

        st.subheader("📈 Threat Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", total_rows)
        col2.metric("Anomalies Detected", anomaly_count)
        col3.metric("Anomaly Percentage", f"{anomaly_percentage:.2f}%")

        health_score = 100 - anomaly_percentage

        if health_score > 90:
            status = "🟢 Healthy"
        elif health_score > 70:
            status = "🟡 Moderate Risk"
        else:
            status = "🔴 High Risk"

        st.progress(int(health_score))
        st.write(f"Threat Level: **{status}**")

        st.subheader("🚨 Flagged Traffic")
        st.dataframe(
            processed_data[processed_data["anomaly"] == "Anomalous"]
        )
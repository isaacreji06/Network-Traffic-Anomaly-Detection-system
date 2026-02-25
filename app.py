import streamlit as st

st.set_page_config(page_title="Network IDS", layout="wide")

st.title("🛡️ Intelligent Network Intrusion Detection System")

st.markdown("""
### Protecting Networks Using Machine Learning

Traditional rule-based intrusion detection systems often miss novel attacks 
or generate excessive false positives.

This system uses **machine learning-based anomaly detection** to identify 
suspicious network behavior in real time.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 What This System Does")
    st.markdown("""
    - Detects abnormal traffic patterns
    - Reduces false positives
    - Provides real-time threat indicators
    - Visualizes suspicious activity
    """)

with col2:
    st.subheader("👥 Who It Helps")
    st.markdown("""
    - Network Security Analysts  
    - IT Administrators  
    - Enterprises with critical infrastructure  
    """)

st.markdown("---")

st.success("Use the sidebar to begin monitoring your network traffic.")
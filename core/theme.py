import streamlit as st

def apply_modern_theme():
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #0f172a, #020617);
        color: #e2e8f0;
        font-family: 'Segoe UI', sans-serif;
    }

    div[data-testid="metric-container"] {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(0,255,255,0.2);
        border-radius: 16px;
        padding: 15px;
        backdrop-filter: blur(10px);
        box-shadow: 0px 0px 20px rgba(0,255,255,0.1);
        transition: 0.3s ease;
    }

    div[data-testid="metric-container"]:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 35px rgba(124,58,237,0.5);
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 5px #06b6d4; }
        50% { box-shadow: 0 0 25px #7c3aed; }
        100% { box-shadow: 0 0 5px #06b6d4; }
    }

    .threat-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        animation: pulse 2s infinite;
    }
    </style>
    """, unsafe_allow_html=True)
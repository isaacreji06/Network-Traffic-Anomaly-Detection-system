import streamlit as st

def initialize_state():
    defaults = {
        "raw_data": None,
        "processed_data": None,
        "detector": None,
        "threat_index": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
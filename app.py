import streamlit as st

st.set_page_config(
    page_title="SENTINEL IDS",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* Remove Streamlit UI */
#MainMenu, footer, header {visibility:hidden;}
[data-testid="collapsedControl"] {display:none;}
[data-testid="stSidebar"] {display:none;}
.block-container {padding:0 !important; margin:0 !important; max-width:100% !important;}

/* Remove scrolling */
html, body, .stApp {
    margin:0 !important;
    padding:0 !important;
    height:100%;
    overflow:hidden !important;
    background: linear-gradient(180deg, #000814 0%, #001d3d 100%);
    color:#00f5ff;
    font-family: 'Courier New', monospace;
}

/* Fullscreen Hero */
.hero {
    position: fixed;
    inset: 0;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    width: 100vw;
    height: 100vh;

    text-align: center;
    padding: 0 5vw;
}

/* Typography */
.title {
    font-size: 80px;
    font-weight: 900;
    letter-spacing: 8px;
    text-shadow: 0 0 30px rgba(0,245,255,0.8);
}

.subtitle {
    font-size: 18px;
    letter-spacing: 4px;
    opacity: 0.7;
    margin-top: 10px;
}

.description {
    max-width: 750px;
    margin: 40px auto 0 auto;
    font-size: 16px;
    opacity: 0.75;
    line-height: 1.8;
}

/* Status bar centered */
.status-bar {
    display: flex;
    justify-content: center;
    gap: 60px;
    margin-top: 40px;
    font-size: 14px;
}

.status-dot {
    height: 10px;
    width: 10px;
    background: #00ff88;
    border-radius: 50%;
    display: inline-block;
    margin-right: 8px;
    box-shadow: 0 0 12px #00ff88;
}

/* Center button wrapper */
.stButton {
    display: flex;
    justify-content: center;
}

/* Button style */
.stButton > button {
    margin-top: 50px;
    background: transparent !important;
    border: 2px solid #00f5ff !important;
    color: #00f5ff !important;
    padding: 15px 60px !important;
    font-size: 16px !important;
    letter-spacing: 2px !important;
    transition: 0.3s ease !important;
}

./* HARD CENTER STREAMLIT BUTTON */
.stButton {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
}

.stButton > button {
    margin: 50px auto 0 auto !important;
}

</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero">', unsafe_allow_html=True)

st.markdown('<div class="title">‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎     SENTINEL</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎ ‎  ‎ ‎ ‎ ‎‎ ‎   ‎ ‎ ‎ ‎‎ ‎  ‎ ‎ ‎ ‎‎ ‎  ‎ ‎ ‎ ‎‎ ‎  ‎ ‎ ‎ ‎‎ ‎  ‎ ‎ ‎ ‎‎ ‎  ‎ ‎ ‎ ‎‎ ‎  ‎ ‎ ‎ INTELLIGENT INTRUSION DETECTION SYSTEM</div>', unsafe_allow_html=True)

st.markdown("""
<div class="description">
Advanced anomaly detection powered by Isolation Forest Machine Learning.
Upload network traffic data and instantly identify suspicious patterns,
reduce false positives, and monitor your system in real-time —
without needing labeled datasets.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="status-bar">
    <div><span class="status-dot"></span> SYSTEM ONLINE</div>
    <div><span class="status-dot"></span> ML ENGINE READY</div>
    <div><span class="status-dot"></span> MONITORING ACTIVE</div>
</div>
""", unsafe_allow_html=True)

if st.button("⬡  LAUNCH DETECTION SYSTEM  ⬡"):
    st.switch_page("pages/1_detect.py")

st.markdown('</div>', unsafe_allow_html=True)
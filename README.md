# SENTINEL — Intelligent Network Intrusion Detection System

## Quick Start

bash
# 1. Install dependencies
pip install streamlit pandas numpy scikit-learn plotly

# 2. Run the app
streamlit run app.py


## Project Structure


sentinel_ids_app/
├── app.py                     ← Landing page (run this)
├── requirements.txt
├── pages/
│   ├── 1_detect.py            ← Detection engine + threat dashboard
│   ├── 2_analytics.py         ← PCA maps, distributions, feature correlations
│   └── 3_model.py             ← Model info, specs, pipeline
└── README.md

## Features

- **Futuristic cyberpunk UI** — animated grid background, scan lines, glowing cyan theme
- **No sidebar** — full page-to-page navigation like a real web app
- **Landing page** → Detection → Analytics → Model Info flow
- **Upload your own CSV** or use built-in demo traffic data
- **Isolation Forest ML** — unsupervised anomaly detection, no labels needed
- **Interactive visualizations** — PCA anomaly map, score histograms, feature distributions, timeline
- **Downloadable results** — full results + threats-only CSV exports
- **Adjustable sensitivity** — contamination rate and model strength sliders

## Compatible Datasets

- CICIDS2017 (Monday-WorkingHours.pcap_ISCX.csv, etc.)
- NSL-KDD
- UNSW-NB15
- Any CSV with numeric network traffic features

## Navigation Flow


🌐 app.py (Landing)
      ↓  [LAUNCH DETECTION SYSTEM]
📊 pages/1_detect.py (Upload + Scan)
      ↓  [VIEW ANALYTICS]
📈 pages/2_analytics.py (PCA, distributions)
      ↓  [MODEL INFO]
🧠 pages/3_model.py (Algorithm details)
import streamlit as st

st.title("ℹ️ About the Detection Model")

st.markdown("""
### Model Used: Isolation Forest

Isolation Forest detects anomalies by:
- Randomly partitioning feature space
- Identifying points that are easier to isolate
- Marking isolated points as anomalies

### Why This Approach?

- Works without labeled data
- Efficient for large datasets
- Suitable for detecting novel attack patterns

### Limitations

- Does not classify attack types
- Requires numeric features
- Threshold selection affects sensitivity
""")
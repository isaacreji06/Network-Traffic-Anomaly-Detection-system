import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def run_anomaly_detection(dataframe):
    numeric_data = dataframe.select_dtypes(include=["number"])

    if numeric_data.shape[1] == 0:
        return None, None

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)

    model = IsolationForest(
        n_estimators=150,
        contamination=0.05,
        random_state=42
    )

    model.fit(scaled_data)
    predictions = model.predict(scaled_data)

    dataframe["anomaly"] = predictions
    dataframe["anomaly"] = dataframe["anomaly"].map(
        {1: "Normal", -1: "Anomalous"}
    )

    return dataframe, model
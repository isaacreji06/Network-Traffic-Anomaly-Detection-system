import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


class NetworkAnomalyDetector:
    def __init__(self, contamination=0.05):
        self.scaler = StandardScaler()
        self.model = IsolationForest(
            n_estimators=300,
            contamination=contamination,
            random_state=42
        )

    def fit_predict(self, dataframe):
        numeric_data = dataframe.select_dtypes(include=["number"])

        if numeric_data.empty:
            raise ValueError("No numeric features available.")

        scaled_data = self.scaler.fit_transform(numeric_data)

        self.model.fit(scaled_data)

        predictions = self.model.predict(scaled_data)
        scores = self.model.decision_function(scaled_data)

        result_df = dataframe.copy()
        result_df["anomaly_flag"] = predictions
        result_df["anomaly_label"] = result_df["anomaly_flag"].map(
            {1: "Normal", -1: "Anomalous"}
        )
        result_df["anomaly_score"] = scores

        return result_df
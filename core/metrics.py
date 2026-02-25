def calculate_threat_index(dataframe):
    total = len(dataframe)
    anomalies = (dataframe["anomaly_label"] == "Anomalous").sum()

    if total == 0:
        return 0

    return round((anomalies / total) * 100, 2)
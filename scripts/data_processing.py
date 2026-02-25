"""
Network Traffic Anomaly Detection System
Data Processing Module

Demonstrates:
- Conditional logic
- Loop structures
- Function definitions
- Data flow using return values
- Structured, reusable code organization
"""

# ========================
# Imports
# ========================

import pandas as pd
from pathlib import Path


# ========================
# Core Data Processing Functions
# ========================

def load_raw_data(file_path):
    """Load raw network traffic data from a CSV file."""
    print(f"Loading raw data from {file_path}")
    return pd.read_csv(file_path)


def clean_data(dataframe):
    """Perform basic preprocessing and validation."""

    if dataframe.empty:
        print("Dataset is empty.")
        return dataframe

    duplicate_row_count = dataframe.duplicated().sum()
    if duplicate_row_count > 0:
        dataframe = dataframe.drop_duplicates()

    missing_value_count = dataframe.isnull().sum().sum()
    if missing_value_count > 0:
        dataframe = dataframe.dropna()

    return dataframe


def save_processed_data(dataframe, output_path):
    """Save cleaned dataset to processed folder."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)


# ========================
# Analytical Utility Functions
# ========================

def calculate_packet_ratio(incoming_packets, outgoing_packets):
    """Return ratio of incoming to outgoing packets."""
    if outgoing_packets == 0:
        return None
    return incoming_packets / outgoing_packets


def classify_traffic(packet_ratio):
    """Classify traffic pattern based on packet ratio."""
    if packet_ratio is None:
        return "Undefined (division by zero)"
    if packet_ratio > 1.5:
        return "High Incoming Traffic"
    if packet_ratio < 0.5:
        return "High Outgoing Traffic"
    return "Balanced Traffic"


# ========================
# Demonstration Functions
# ========================

def demonstrate_loops():
    """Show basic loop usage."""

    for iteration_number in range(3):
        print(f"Iteration: {iteration_number}")

    status_list = ["normal", "anomaly", "normal"]
    for status in status_list:
        if status == "anomaly":
            print("Anomaly detected.")
            continue
        print("Traffic normal.")


def demonstrate_data_flow():
    """Demonstrate passing data into functions and using return values."""

    incoming_packet_count = 300
    outgoing_packet_count = 150

    packet_ratio = calculate_packet_ratio(
        incoming_packet_count,
        outgoing_packet_count
    )

    traffic_classification = classify_traffic(packet_ratio)

    print(f"Packet ratio: {packet_ratio}")
    print(f"Traffic classification: {traffic_classification}")


# ========================
# Main Execution Pipeline
# ========================

def main():
    """Main entry point of the script."""

    project_root = Path(__file__).resolve().parent.parent

    raw_data_path = project_root / "data" / "raw" / "Monday-WorkingHours.pcap_ISCX.csv"
    processed_data_path = project_root / "data" / "processed" / "network_data_cleaned.csv"

    if raw_data_path.exists():
        raw_dataframe = load_raw_data(raw_data_path)
        cleaned_dataframe = clean_data(raw_dataframe)
        save_processed_data(cleaned_dataframe, processed_data_path)
    else:
        print("Raw data not found. Skipping data loading.")

    print("\nData pipeline execution complete.\n")

    demonstrate_loops()
    demonstrate_data_flow()


# ========================
# Script Entry Point
# ========================

if __name__ == "__main__":
    main()
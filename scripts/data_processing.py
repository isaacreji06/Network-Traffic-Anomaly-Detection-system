"""
Network Traffic Anomaly Detection System
Data Processing Module

Demonstrates:
- Conditional logic
- Loop structures
- Function definitions
- Data flow using return values
- Basic PEP 8 readability standards
"""

import pandas as pd
from pathlib import Path


def load_raw_data(file_path):
    """
    Load raw network traffic data from a CSV file.
    Raw data should never be modified directly.
    """
    print(f"Loading raw data from {file_path}")
    dataframe = pd.read_csv(file_path)
    return dataframe


def clean_data(dataframe):
    """
    Perform basic preprocessing to ensure data integrity.
    """

    print("Starting basic data cleaning...")

    # Ensure dataset is not empty before processing
    if dataframe.empty:
        print("Warning: Dataset is empty.")
        return dataframe

    print(f"Initial row count: {len(dataframe)}")

    # Remove duplicate rows if present
    duplicate_row_count = dataframe.duplicated().sum()
    if duplicate_row_count > 0:
        print(f"Removing {duplicate_row_count} duplicate rows.")
        dataframe = dataframe.drop_duplicates()
    else:
        print("No duplicate rows found.")

    # Remove rows with missing values
    missing_value_count = dataframe.isnull().sum().sum()
    if missing_value_count > 0:
        print(f"Removing rows with {missing_value_count} missing values.")
        dataframe = dataframe.dropna()
    else:
        print("No missing values detected.")

    total_row_count = len(dataframe)

    if total_row_count > 100000:
        print("Large dataset detected.")
    elif total_row_count > 10000:
        print("Moderate dataset size.")
    else:
        print("Small dataset.")

    if total_row_count > 0:
        print("Dataset is valid for further analysis.")
    else:
        print("Dataset is not valid for analysis.")

    print("Cleaning completed.")
    return dataframe


def save_processed_data(dataframe, output_path):
    """
    Save cleaned data to the processed data folder.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")


def loop_demonstration():
    """
    Demonstrate usage of for and while loops.
    """

    print("\n--- Loop Demonstration ---")

    print("\nFor loop over range:")
    for iteration_number in range(5):
        print(f"Iteration number: {iteration_number}")

    print("\nFor loop over list:")
    traffic_status_list = ["normal", "normal", "anomaly", "normal"]

    for traffic_status in traffic_status_list:
        if traffic_status == "anomaly":
            print("Anomaly detected in traffic.")
            continue
        print("Traffic is normal.")

    print("\nWhile loop example:")
    attempt_counter = 0

    while attempt_counter < 3:
        print(f"Counter value: {attempt_counter}")
        attempt_counter += 1

    print("\nBreak example:")
    for value in range(10):
        if value == 4:
            print("Stopping loop at value 4.")
            break
        print(f"Value: {value}")


def calculate_packet_ratio(incoming_packets, outgoing_packets):
    """
    Calculate ratio of incoming to outgoing packets.
    Returns None if division is not possible.
    """
    if outgoing_packets == 0:
        return None

    return incoming_packets / outgoing_packets


def classify_traffic(packet_ratio):
    """
    Classify traffic pattern based on packet ratio.
    """
    if packet_ratio is None:
        return "Undefined (division by zero)"

    if packet_ratio > 1.5:
        return "High Incoming Traffic"
    if packet_ratio < 0.5:
        return "High Outgoing Traffic"

    return "Balanced Traffic"


def main():
    """
    Main execution pipeline.
    """

    project_root = Path(__file__).resolve().parent.parent

    raw_data_path = project_root / "data" / "raw" / "Monday-WorkingHours.pcap_ISCX.csv"
    processed_data_path = project_root / "data" / "processed" / "network_data_cleaned.csv"

    if not raw_data_path.exists():
        print("Raw data not found. Skipping data loading.")
    else:
        raw_dataframe = load_raw_data(raw_data_path)
        cleaned_dataframe = clean_data(raw_dataframe)
        save_processed_data(cleaned_dataframe, processed_data_path)

    print("\nData processing pipeline completed successfully.")

    loop_demonstration()

    print("\n--- Data Flow Demonstration ---")

    incoming_packet_count = 300
    outgoing_packet_count = 150

    packet_ratio = calculate_packet_ratio(
        incoming_packet_count,
        outgoing_packet_count
    )

    traffic_classification = classify_traffic(packet_ratio)

    print(f"Incoming packets: {incoming_packet_count}")
    print(f"Outgoing packets: {outgoing_packet_count}")
    print(f"Packet ratio: {packet_ratio}")
    print(f"Traffic classification: {traffic_classification}")


if __name__ == "__main__":
    main()
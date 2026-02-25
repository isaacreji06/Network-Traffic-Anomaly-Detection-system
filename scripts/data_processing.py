import pandas as pd
from pathlib import Path


def load_raw_data(file_path):
    """
    Load raw network traffic data from CSV.
    Raw data should never be modified directly.
    """
    print(f"Loading raw data from {file_path}")
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Perform basic preprocessing with conditional logic.
    """

    print("Starting basic data cleaning...")

    # 1️⃣ Conditional check before cleaning
    if df.empty:
        print("⚠️ Warning: DataFrame is empty.")
        return df
    else:
        print(f"Initial rows: {len(df)}")

    # 2️⃣ Drop duplicates
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:
        print(f"Found {duplicate_count} duplicate rows. Removing them...")
        df = df.drop_duplicates()
    else:
        print("No duplicate rows found.")

    # 3️⃣ Handle missing values using conditional logic
    missing_count = df.isnull().sum().sum()

    if missing_count > 0:
        print(f"Found {missing_count} missing values. Dropping rows with missing data.")
        df = df.dropna()
    else:
        print("No missing values detected.")

    # 4️⃣ Example of multi-branch conditional (traffic-based logic)
    row_count = len(df)

    if row_count > 100000:
        print("Large dataset detected.")
    elif row_count > 10000:
        print("Moderate dataset size.")
    else:
        print("Small dataset.")

    # 5️⃣ Logical operators example
    if row_count > 0 and not df.empty:
        print("Dataset is valid for further analysis.")
    else:
        print("Dataset is not valid for analysis.")

    print("Cleaning completed.")
    return df


def save_processed_data(df, output_path):
    """
    Save processed data to processed folder.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

def loop_demonstration():
    """
    Milestone 4.17 - Loop Demonstration

    
    """

    print("\n--- Loop Demonstration ---")

    # 1️⃣ FOR LOOP - Iterating over range
    print("\nFor loop over range:")
    for i in range(5):
        print(f"Iteration number: {i}")

    # 2️⃣ FOR LOOP - Iterating over list
    print("\nFor loop over list:")
    network_status = ["normal", "normal", "anomaly", "normal"]

    for status in network_status:
        if status == "anomaly":
            print("⚠️ Anomaly detected in traffic")
            continue  # Skip remaining logic for this iteration
        print("Traffic is normal")

    # 3️⃣ WHILE LOOP - Condition-based repetition
    print("\nWhile loop example:")
    counter = 0

    while counter < 3:
        print(f"Counter value: {counter}")
        counter += 1  # Critical: updating variable to avoid infinite loop

    # 4️⃣ BREAK example
    print("\nBreak example:")
    for value in range(10):
        if value == 4:
            print("Breaking loop at value 4")
            break
        print(f"Value: {value}")

    # 5️⃣ Safe loop with condition check
    print("\nSafe while loop with condition:")
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        print(f"Attempt {attempts}")
        attempts += 1

        if attempts == 3:
            print("Stopping early using break")
            break


def main():
    # Resolve project root
    project_root = Path(__file__).resolve().parent.parent

    # Paths
    raw_data_path = project_root / "data" / "raw" / "Monday-WorkingHours.pcap_ISCX.csv"
    processed_data_path = project_root / "data" / "processed" / "network_data_cleaned.csv"

    # Conditional file check
    if not raw_data_path.exists():
        print("Raw data not found. Skipping data loading for now.")
        df_cleaned = None
    else:
        df_raw = load_raw_data(raw_data_path)
        df_cleaned = clean_data(df_raw)
        save_processed_data(df_cleaned, processed_data_path)

    print("Data processing pipeline completed successfully.")

    # Loop demonstration (Milestone 4.17)
    loop_demonstration()


if __name__ == "__main__":
    main()

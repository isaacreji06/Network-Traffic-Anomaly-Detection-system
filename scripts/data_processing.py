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


def main():
    # Resolve project root so paths work regardless of where the script is invoked
    project_root = Path(__file__).resolve().parent.parent

    # Paths
    raw_data_path = project_root / "data" / "raw" / "Monday-WorkingHours.pcap_ISCX.csv"
    processed_data_path = project_root / "data" / "processed" / "network_data_cleaned.csv"

    if not raw_data_path.exists():
        available = list((project_root / "data" / "raw").glob("*.csv"))
        if available:
            details = "Available files: " + ", ".join(p.name for p in available)
        else:
            details = "No CSV files found in data/raw."
        raise FileNotFoundError(f"Raw data file not found at {raw_data_path}. {details}")

    # Pipeline
    df_raw = load_raw_data(raw_data_path)
    df_cleaned = clean_data(df_raw)
    save_processed_data(df_cleaned, processed_data_path)

    print("Data processing pipeline completed successfully.")


if __name__ == "__main__":
    main()

# scripts/train_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

def train_and_save_model(data_path, model_save_path):
    print(f"Loading data from {data_path}...")
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        print("Data file not found. Please provide a valid CSV file.")
        return

    # 1. Feature Selection (Using basic traffic features as per your scope)
    # Ensure these columns match your dataset (e.g., CICIDS2017)
    features = [
        'Total Length of Fwd Packets', 
        'Total Length of Bwd Packets',
        'Flow Duration', 
        'Total Fwd Packets', 
        'Total Backward Packets'
    ]
    
    # 2. Preprocessing
    df.columns = df.columns.str.strip() # Clean column names
    available_features = [f for f in features if f in df.columns]
    
    if not available_features:
        print("Required features not found in the dataset.")
        return

    X = df[available_features].fillna(0) # Handle missing values

    # 3. Model Training
    print("Training Isolation Forest model...")
    # Contamination is the expected proportion of anomalies (e.g., 5%)
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(X)

    # 4. Save the Model
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    joblib.dump(model, model_save_path)
    print(f"Model saved successfully to {model_save_path}")

if __name__ == "__main__":
    # Adjust paths based on your folder structure
    INPUT_DATA = "../data/processed/network_data_cleaned.csv" 
    MODEL_OUTPUT = "../models/isolation_forest.pkl"
    train_and_save_model(INPUT_DATA, MODEL_OUTPUT)
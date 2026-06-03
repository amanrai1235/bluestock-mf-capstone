import pandas as pd
import os

# Paths
raw_path = "data/raw"
processed_path = "data/processed"

# Processed folder create if not exists
os.makedirs(processed_path, exist_ok=True)

# Files to clean
files = [
    "02_nav_history.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
]

for file in files:
    print(f"\nProcessing {file}")

    # Read CSV
    df = pd.read_csv(f"{raw_path}/{file}")

    print("Shape Before:", df.shape)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values using forward fill
    df.ffill(inplace=True)

    print("Shape After:", df.shape)

    # Save cleaned file
    df.to_csv(f"{processed_path}/{file}", index=False)

print("\nCleaning Completed Successfully!")
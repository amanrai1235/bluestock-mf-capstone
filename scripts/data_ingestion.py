import pandas as pd
import os

folder_path = "data/raw"

print("=" * 60)
print("BLUESTOCK MF DATA INGESTION")
print("=" * 60)

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        filepath = os.path.join(folder_path, file)

        print("\n")
        print("=" * 60)
        print("FILE:", file)

        df = pd.read_csv(filepath)

        print("Shape:", df.shape)
        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

print("\nAll datasets loaded successfully.")
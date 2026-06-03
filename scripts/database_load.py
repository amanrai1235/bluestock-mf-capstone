import pandas as pd
from sqlalchemy import create_engine

# SQLite database
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Read cleaned files
nav = pd.read_csv("data/processed/02_nav_history.csv")
performance = pd.read_csv("data/processed/07_scheme_performance.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions.csv")

# Load into SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

print("Database Loaded Successfully!")
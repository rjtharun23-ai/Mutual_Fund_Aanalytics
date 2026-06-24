import pandas as pd
import os
from sqlalchemy import create_engine

os.makedirs("data/db", exist_ok=True)

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

tables = {
    "dim_fund": "data/raw/01_fund_master.csv",
    "fact_nav": "data/processed/clean_nav.csv",
    "fact_transactions": "data/processed/clean_transactions.csv",
    "fact_performance": "data/processed/clean_performance.csv",
    "fact_aum": "data/raw/03_aum_by_fund_house.csv",
    "fact_sip": "data/raw/04_monthly_sip_inflows.csv",
    "fact_benchmark": "data/raw/10_benchmark_indices.csv"
}

for table_name, file_path in tables.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(table_name, "loaded")

print("SQLite database created successfully")
import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# Clean NAV data
nav = pd.read_csv("data/raw/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]
nav["daily_return_pct"] = nav.groupby("amfi_code")["nav"].pct_change() * 100
nav.to_csv("data/processed/clean_nav.csv", index=False)

# Clean transaction data
tx = pd.read_csv("data/raw/08_investor_transactions.csv")
tx["transaction_date"] = pd.to_datetime(tx["transaction_date"])
tx["transaction_type"] = tx["transaction_type"].str.strip().str.title()
tx["kyc_status"] = tx["kyc_status"].str.strip().str.title()
tx = tx[tx["amount_inr"] > 0]
tx = tx[tx["transaction_type"].isin(["Sip", "Lumpsum", "Redemption"])]
tx = tx[tx["kyc_status"].isin(["Verified", "Pending"])]
tx.to_csv("data/processed/clean_transactions.csv", index=False)

# Clean performance data
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
perf["negative_sharpe_flag"] = perf["sharpe_ratio"] < 0
perf["expense_ratio_valid"] = perf["expense_ratio_pct"].between(0.1, 2.5)
perf.to_csv("data/processed/clean_performance.csv", index=False)

print("Data cleaning completed successfully")
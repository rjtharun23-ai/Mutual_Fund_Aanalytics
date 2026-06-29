import pandas as pd

# Read NAV data
df = pd.read_csv("data/processed/clean_nav.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort data
df = df.sort_values(["amfi_code", "date"])

result = []

# Calculate CAGR for each fund
for code, group in df.groupby("amfi_code"):

    start_nav = group.iloc[0]["nav"]
    end_nav = group.iloc[-1]["nav"]

    start_date = group.iloc[0]["date"]
    end_date = group.iloc[-1]["date"]

    years = (end_date - start_date).days / 365

    cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

    result.append([code, round(cagr, 2)])

# Save result
cagr_df = pd.DataFrame(result, columns=["amfi_code", "CAGR (%)"])

cagr_df.to_csv("data/processed/fund_cagr.csv", index=False)

print("CAGR calculated successfully")
import pandas as pd

# Read cleaned NAV data
df = pd.read_csv("data/processed/clean_nav.csv")

# Convert date column into datetime format
df["date"] = pd.to_datetime(df["date"])

# Arrange data properly
df = df.sort_values(["amfi_code", "date"])

# Calculate daily return for each fund
df["daily_return"] = df.groupby("amfi_code")["nav"].pct_change()

# Save result
df.to_csv("data/processed/daily_returns.csv", index=False)

print("Daily returns calculated successfully")
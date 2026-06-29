import pandas as pd
from scipy.stats import linregress

# Read daily fund returns
returns = pd.read_csv("data/processed/daily_returns.csv")
returns["date"] = pd.to_datetime(returns["date"])

# Read benchmark data
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")
benchmark["date"] = pd.to_datetime(benchmark["date"])

# Use NIFTY50 as benchmark
nifty = benchmark[benchmark["index_name"] == "NIFTY50"].copy()
nifty = nifty.sort_values("date")
nifty["benchmark_return"] = nifty["close_value"].pct_change()

result = []

# Calculate alpha and beta for each fund
for code, group in returns.groupby("amfi_code"):

    group = group[["date", "daily_return"]].dropna()

    merged = pd.merge(group, nifty[["date", "benchmark_return"]], on="date")
    merged = merged.dropna()

    if len(merged) < 2:
        continue

    beta, alpha_daily, r_value, p_value, std_error = linregress(
        merged["benchmark_return"],
        merged["daily_return"]
    )

    alpha_annual = alpha_daily * 252

    result.append([
        code,
        round(alpha_annual, 4),
        round(beta, 4)
    ])

alpha_beta = pd.DataFrame(
    result,
    columns=["amfi_code", "Alpha", "Beta"]
)

alpha_beta.to_csv("data/processed/alpha_beta.csv", index=False)

print("Alpha and Beta calculated successfully")
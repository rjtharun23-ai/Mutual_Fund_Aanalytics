import pandas as pd

# Read daily returns
df = pd.read_csv("data/processed/daily_returns.csv")

result = []

# Calculate Sharpe and Sortino for each fund
for code, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) == 0:
        continue

    mean_return = returns.mean()

    std_return = returns.std()

    downside = returns[returns < 0]

    downside_std = downside.std()

    sharpe = (mean_return / std_return) * (252 ** 0.5)

    if pd.isna(downside_std) or downside_std == 0:
        sortino = 0
    else:
        sortino = (mean_return / downside_std) * (252 ** 0.5)

    result.append([
        code,
        round(sharpe, 2),
        round(sortino, 2)
    ])

result_df = pd.DataFrame(
    result,
    columns=["amfi_code", "Sharpe Ratio", "Sortino Ratio"]
)

result_df.to_csv(
    "data/processed/sharpe_sortino.csv",
    index=False
)

print("Sharpe and Sortino calculated successfully")
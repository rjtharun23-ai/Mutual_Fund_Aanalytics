import pandas as pd

# Read NAV data
df = pd.read_csv("data/processed/clean_nav.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["amfi_code", "date"])

result = []

for code, group in df.groupby("amfi_code"):

    group = group.copy()

    group["running_max"] = group["nav"].cummax()
    group["drawdown"] = (group["nav"] / group["running_max"]) - 1

    max_drawdown = group["drawdown"].min()
    worst_date = group.loc[group["drawdown"].idxmin(), "date"]

    result.append([
        code,
        round(max_drawdown * 100, 2),
        worst_date.date()
    ])

drawdown_df = pd.DataFrame(
    result,
    columns=["amfi_code", "Max Drawdown (%)", "Worst Drawdown Date"]
)

drawdown_df.to_csv("data/processed/max_drawdown.csv", index=False)

print("Maximum drawdown calculated successfully")
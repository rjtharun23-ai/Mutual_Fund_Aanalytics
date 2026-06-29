import pandas as pd
import os

os.makedirs("reports", exist_ok=True)

fund = pd.read_csv("data/raw/01_fund_master.csv")
cagr = pd.read_csv("data/processed/fund_cagr.csv")
sharpe = pd.read_csv("data/processed/sharpe_sortino.csv")
alpha_beta = pd.read_csv("data/processed/alpha_beta.csv")
drawdown = pd.read_csv("data/processed/max_drawdown.csv")

scorecard = fund[["amfi_code", "fund_house", "scheme_name", "category", "risk_category"]]

scorecard = scorecard.merge(cagr, on="amfi_code")
scorecard = scorecard.merge(sharpe, on="amfi_code")
scorecard = scorecard.merge(alpha_beta, on="amfi_code")
scorecard = scorecard.merge(drawdown, on="amfi_code")

scorecard["score"] = (
    scorecard["CAGR (%)"].rank(pct=True) * 30 +
    scorecard["Sharpe Ratio"].rank(pct=True) * 25 +
    scorecard["Alpha"].rank(pct=True) * 20 +
    scorecard["Max Drawdown (%)"].rank(pct=True, ascending=False) * 25
)

scorecard["score"] = scorecard["score"].round(2)

scorecard = scorecard.sort_values("score", ascending=False)

scorecard.to_csv("reports/fund_scorecard.csv", index=False)

print("Fund scorecard created successfully")
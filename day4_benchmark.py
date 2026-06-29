import pandas as pd
import plotly.express as px
import os

os.makedirs("charts", exist_ok=True)

scorecard = pd.read_csv("reports/fund_scorecard.csv")

top5 = scorecard.head(5)

chart_data = top5[[
    "scheme_name",
    "CAGR (%)",
    "Sharpe Ratio",
    "Alpha",
    "Beta",
    "score"
]]

fig = px.bar(
    chart_data,
    x="scheme_name",
    y="score",
    title="Top 5 Funds by Performance Score",
    text="score"
)

fig.update_layout(xaxis_tickangle=-45)

fig.write_image("charts/day4_top5_funds_score.png")

fig.show()

print("Benchmark comparison chart created successfully")
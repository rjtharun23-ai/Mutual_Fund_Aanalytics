
-- Day 2 SQLite Schema

CREATE TABLE dim_fund (
    amfi_code INTEGER,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    date DATE,
    nav REAL,
    daily_return_pct REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr INTEGER,
    state TEXT,
    city TEXT,
    kyc_status TEXT
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,
    aum_crore INTEGER
);

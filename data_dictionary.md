# Data Dictionary

## dim_fund
amfi_code - Unique AMFI scheme code
fund_house - Mutual fund company name
scheme_name - Name of the mutual fund scheme
category - Equity or Debt
sub_category - Large Cap, Small Cap, etc.
risk_category - Risk classification

## fact_nav
amfi_code - Fund code
date - NAV date
nav - Net Asset Value
daily_return_pct - Daily percentage return

## fact_transactions
investor_id - Unique investor identifier
transaction_date - Date of transaction
transaction_type - SIP, Lumpsum, Redemption
amount_inr - Transaction amount
state - Investor state
city - Investor city
kyc_status - Verification status

## fact_performance
return_1yr_pct - 1 year return
return_3yr_pct - 3 year return
sharpe_ratio - Risk adjusted return measure
expense_ratio_pct - Fund expense ratio
aum_crore - Assets under management
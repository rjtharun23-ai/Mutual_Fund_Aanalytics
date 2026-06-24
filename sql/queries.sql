
-- 1. Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by fund
SELECT amfi_code, AVG(nav) AS average_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. SIP inflow trend
SELECT month, sip_inflow_crore
FROM fact_sip;

-- 4. Transactions by state
SELECT state, COUNT(*) AS total_transactions, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 5 funds by 3-year return
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 7. Transaction type summary
SELECT transaction_type, COUNT(*) AS total_count, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 8. Average transaction amount by age group
SELECT age_group, AVG(amount_inr) AS average_amount
FROM fact_transactions
GROUP BY age_group;

-- 9. Benchmark average close value
SELECT index_name, AVG(close_value) AS average_close
FROM fact_benchmark
GROUP BY index_name;

-- 10. Fund count by category
SELECT category, COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;

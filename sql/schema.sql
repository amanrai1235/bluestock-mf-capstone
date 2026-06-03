CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT
);

CREATE TABLE fact_nav (
    id INTEGER PRIMARY KEY,
    nav REAL
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    amount REAL
);

CREATE TABLE fact_performance (
    id INTEGER PRIMARY KEY,
    return_percent REAL
);
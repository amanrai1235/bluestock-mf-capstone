-- 1
SELECT COUNT(*) FROM fact_nav;

-- 2
SELECT AVG(nav) FROM fact_nav;

-- 3
SELECT MAX(nav) FROM fact_nav;

-- 4
SELECT MIN(nav) FROM fact_nav;

-- 5
SELECT * FROM fact_nav LIMIT 10;

-- 6
SELECT COUNT(*) FROM fact_transactions;

-- 7
SELECT AVG(amount) FROM fact_transactions;

-- 8
SELECT MAX(amount) FROM fact_transactions;

-- 9
SELECT * FROM fact_performance LIMIT 10;

-- 10
SELECT COUNT(*) FROM fact_performance;
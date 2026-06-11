# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview

This capstone project focuses on Mutual Fund Analytics using Python, SQL, and Power BI. The objective is to analyze mutual fund performance, investor behavior, portfolio risk, and benchmark comparisons to generate actionable insights for investors and fund managers.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* Power BI
* Git & GitHub

---

## Project Architecture

Data Sources → Data Cleaning → SQLite Database → Python Analytics → Risk Analysis → Power BI Dashboard → Insights & Recommendations

---

## Dataset Description

The project uses multiple datasets including:

1. Fund Master Data
2. NAV History
3. AUM Data
4. SIP Inflows
5. Category Inflows
6. Scheme Performance
7. Investor Transactions
8. Portfolio Holdings
9. Benchmark Indices
10. Fund Benchmark Mapping

---

## Folder Structure

* data/raw → Original datasets
* data/processed → Cleaned datasets
* data/db → SQLite database
* scripts → Python ETL scripts
* notebooks → Jupyter notebooks
* sql → SQL queries
* dashboard → Power BI dashboard
* reports → Final reports

---

## Advanced Analytics Performed

### Risk Analytics

* Value at Risk (VaR 95%)
* Conditional Value at Risk (CVaR 95%)

### Performance Analytics

* 90-Day Rolling Sharpe Ratio
* Fund Performance Ranking

### Investor Analytics

* Cohort Analysis
* Investor Retention Analysis
* At-Risk Investor Detection

### Recommendation Engine

* Fund recommendation based on risk profile

---

## Key Findings

* Fund 119599 showed the highest downside risk in VaR analysis.
* Multiple schemes achieved Rolling Sharpe Ratios above 2, indicating strong risk-adjusted performance.
* Investors acquired during 2024 contributed the majority of invested capital.
* Approximately 3900+ investors were identified as At-Risk due to long SIP inactivity periods.
* High-risk investors can be matched with suitable high-growth schemes using the recommendation engine.

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute Pipeline

```bash
python run_pipeline.py
```

### Open Dashboard

Open the Power BI dashboard file:

```text
bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

## Project Outputs

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* advanced_analytics.ipynb
* run_pipeline.py
* rolling_sharpe_chart.png
* var_cvar_report.csv
* cohort_analysis.csv
* recommender_output.csv

---

## Author

Aman Kumar Rai

Bluestock Mutual Fund Analytics Capstone Project – 2026

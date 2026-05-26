# Customer Churn Prediction & Analysis

## Project Overview
Analyzed 7,032 customer records to identify churn drivers and predict 
customer churn using machine learning models.
## Dashboard
[View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/vamsi.batchu8113/viz/CustomerChurnAnalysis_17797607527530/CustomerChurnAnalysisDashboard)
## Key Findings
- Overall churn rate: **26.6%**
- Month-to-month contract churn: **42.7%** vs 2.8% for two-year contracts
- Churned customers stay only **18 months** vs 37.7 months for retained
- Average monthly charges for churned: **$74.44** vs $61.31 retained
- Monthly revenue at risk: **$139,130**

## Models Built
| Model | Accuracy |
|-------|----------|
| Logistic Regression | 80.4% |
| Random Forest | 78.6% |

## Top Churn Predictors
1. Total Charges
2. Tenure Months
3. Monthly Charges
4. Contract Type
5. City

## Tools Used
- Python (Pandas, NumPy, Matplotlib, Scikit-learn)
- SQL
- Tableau
- Power BI

## Files
- `churn_analysis.py` — Complete Python analysis and ML models
- `churn_by_contract.png` — Churn rate by contract type chart
- `feature_importance.png` — Top 5 churn predictors chart
- `churn_clean.csv` — Cleaned dataset for dashboard

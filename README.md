# Customer Churn Prediction & Analysis

I built this project because I wanted to understand what actually drives 
customers to leave a telecom company. Churn is a real business problem 
that affects revenue directly, and I wanted to see if I could predict it 
using machine learning.

## What I Did
I started by exploring the dataset — 7,032 customers with 33 variables 
including contract type, monthly charges, tenure, and internet service. 
The first thing I noticed was how unbalanced the data was — only 26.6% 
of customers actually churned.

The most surprising finding was how dramatically contract type affected 
churn. Month-to-month customers churned at 42.7% while two-year contract 
customers only churned at 2.8%. That's a 15x difference — a massive 
business insight.

I also found that churned customers paid more on average ($74.44/month) 
than retained customers ($61.31/month), which was counterintuitive at first 
— you'd think higher-paying customers would be more loyal, but they're 
actually more likely to leave if they feel they're not getting value.

## Dashboard
[View Interactive Dashboard on Tableau Public](https://public.tableau.com/app/profile/vamsi.batchu8113/viz/CustomerChurnAnalysis_17797607527530/CustomerChurnAnalysisDashboard)

## Key Findings
- Overall churn rate: **26.6%**
- Month-to-month contract churn: **42.7%** vs 2.8% for two-year contracts
- Churned customers stay only **18 months** vs 37.7 months for retained
- Average monthly charges for churned: **$74.44** vs $61.31 retained
- Monthly revenue at risk: **$139,130**

## Models Built
I tried two models to see which performed better:

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 80.4% |
| Random Forest | 78.6% |

Logistic Regression actually performed slightly better here, which makes 
sense given the relatively straightforward relationship between the features 
and churn outcome.

## Top Churn Predictors
These are the features that matter most according to the Random Forest model:
1. Total Charges
2. Tenure Months
3. Monthly Charges
4. Contract Type
5. City

## SQL Analysis
I wrote 8 SQL queries to dig deeper into the data:
- Overall churn rate calculation
- Churn breakdown by contract type
- Average tenure and charges by churn status
- Monthly revenue at risk
- Churn by internet service type
- Churn by payment method
- High risk customer identification
- Revenue impact by contract type

The SQL confirmed what the Python analysis showed — electronic check 
customers churn at 45.3%, the highest of any payment method.

## Tools Used
- Python (Pandas, NumPy, Matplotlib, Scikit-learn)
- SQL
- Tableau

## Files
- `churn_analysis.py` — Complete Python analysis and ML models
- `churn_queries.sql` — 8 SQL business queries
- `run_sql.py` — SQL execution script
- `churn_by_contract.png` — Churn rate by contract type chart
- `feature_importance.png` — Top 5 churn predictors chart
- `churn_clean.csv` — Cleaned dataset for dashboard

## What I Learned
This project taught me that churn prediction isn't just about building 
an accurate model  it's about finding actionable insights. The 42.7% 
churn rate for month-to-month contracts is the kind of finding that a 
business can actually do something about offer incentives to switch 
to annual contracts.

import pandas as pd
import sqlite3

# Load data into SQLite database
df = pd.read_excel('Telco_customer_churn.xlsx', sheet_name='Telco_Churn')
df['Churn'] = df['Churn Label'].map({'Yes': 1, 'No': 0})
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
df = df.dropna(subset=['Total Charges'])

# Create SQLite connection
conn = sqlite3.connect('churn.db')
df.to_sql('churn_data', conn, if_exists='replace', index=False)
print("Database created successfully!")

# Run all queries
queries = {
    "1. Overall Churn Rate": """
        SELECT COUNT(*) as total_customers,
               SUM(Churn) as churned_customers,
               ROUND(AVG(Churn) * 100, 1) as churn_rate_pct
        FROM churn_data
    """,
    "2. Churn Rate by Contract Type": """
        SELECT Contract,
               COUNT(*) as total_customers,
               SUM(Churn) as churned,
               ROUND(AVG(Churn) * 100, 1) as churn_rate_pct
        FROM churn_data
        GROUP BY Contract
        ORDER BY churn_rate_pct DESC
    """,
    "3. Average Tenure by Churn Status": """
        SELECT CASE WHEN Churn = 1 THEN 'Churned' ELSE 'Retained' END as status,
               ROUND(AVG([Tenure Months]), 1) as avg_tenure_months,
               ROUND(AVG([Monthly Charges]), 2) as avg_monthly_charges
        FROM churn_data
        GROUP BY Churn
    """,
    "4. Monthly Revenue at Risk": """
        SELECT ROUND(SUM([Monthly Charges]), 2) as monthly_revenue_at_risk,
               COUNT(*) as churned_customers
        FROM churn_data
        WHERE Churn = 1
    """,
    "5. Churn Rate by Internet Service": """
        SELECT [Internet Service],
               COUNT(*) as total_customers,
               ROUND(AVG(Churn) * 100, 1) as churn_rate_pct
        FROM churn_data
        GROUP BY [Internet Service]
        ORDER BY churn_rate_pct DESC
    """,
    "6. Churn Rate by Payment Method": """
        SELECT [Payment Method],
               COUNT(*) as total_customers,
               ROUND(AVG(Churn) * 100, 1) as churn_rate_pct
        FROM churn_data
        GROUP BY [Payment Method]
        ORDER BY churn_rate_pct DESC
    """,
    "7. High Risk Customers": """
        SELECT CustomerID, Contract, [Monthly Charges],
               [Tenure Months], [Internet Service]
        FROM churn_data
        WHERE Churn = 1 
            AND Contract = 'Month-to-month'
            AND [Monthly Charges] > 70
        ORDER BY [Monthly Charges] DESC
        LIMIT 10
    """,
    "8. Revenue Impact by Contract Type": """
        SELECT Contract,
               COUNT(*) as churned_customers,
               ROUND(SUM([Monthly Charges]), 2) as monthly_revenue_lost
        FROM churn_data
        WHERE Churn = 1
        GROUP BY Contract
        ORDER BY monthly_revenue_lost DESC
    """
}

for name, query in queries.items():
    print(f"\n{'='*50}")
    print(f"{name}")
    print('='*50)
    result = pd.read_sql_query(query, conn)
    print(result.to_string(index=False))

conn.close()
print("\n\nAll SQL queries executed successfully!")
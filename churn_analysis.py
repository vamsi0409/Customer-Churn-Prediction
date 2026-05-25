import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# STEP 1: LOAD DATA
print("Loading data...")
df = pd.read_excel('Telco_customer_churn.xlsx', sheet_name='Telco_Churn')
print(f"Shape: {df.shape}")
print(df.head())
print("\nColumns:", df.columns.tolist())
# STEP 2: DATA CLEANING
print("\nCleaning data...")
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
df = df.dropna(subset=['Total Charges'])
df['Churn'] = df['Churn Label'].map({'Yes': 1, 'No': 0})

churn_rate = df['Churn'].mean() * 100
total_customers = len(df)
churned_customers = df['Churn'].sum()
print(f"Total Customers: {total_customers}")
print(f"Churned Customers: {churned_customers}")
print(f"Overall Churn Rate: {churn_rate:.1f}%")

# STEP 3: KEY INSIGHTS
print("\nChurn Rate by Contract Type:")
contract_churn = df.groupby('Contract')['Churn'].mean() * 100
print(contract_churn)

print("\nAverage Tenure:")
print(f"  Churned: {df[df['Churn']==1]['Tenure Months'].mean():.1f} months")
print(f"  Retained: {df[df['Churn']==0]['Tenure Months'].mean():.1f} months")

print("\nAverage Monthly Charges:")
print(f"  Churned: ${df[df['Churn']==1]['Monthly Charges'].mean():.2f}")
print(f"  Retained: ${df[df['Churn']==0]['Monthly Charges'].mean():.2f}")

revenue_at_risk = df[df['Churn']==1]['Monthly Charges'].sum()
print(f"\nMonthly Revenue at Risk: ${revenue_at_risk:,.2f}")
# STEP 4: MACHINE LEARNING MODEL
print("\nBuilding ML Models...")

# Encode categorical variables
df_model = df.copy()
le = LabelEncoder()
categorical_cols = df_model.select_dtypes(include='object').columns
for col in categorical_cols:
    df_model[col] = le.fit_transform(df_model[col].astype(str))

# Features and target
drop_cols = ['Churn', 'Churn Label', 'Churn Value', 'Churn Score', 
             'Churn Reason', 'CustomerID', 'CLTV']
X = df_model.drop([c for c in drop_cols if c in df_model.columns], axis=1)
y = df_model['Churn']

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Logistic Regression
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)
print(f"\nLogistic Regression Accuracy: {lr_acc*100:.1f}%")
print(classification_report(y_test, lr_pred))

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print(f"\nRandom Forest Accuracy: {rf_acc*100:.1f}%")
print(classification_report(y_test, rf_pred))

# Feature Importance
feat_imp = pd.Series(rf.feature_importances_, 
                     index=X.columns).sort_values(ascending=False).head(5)
print("\nTop 5 Features:")
print(feat_imp)
# STEP 5: SAVE CHARTS
fig, ax = plt.subplots(figsize=(8,5))
contract_churn.plot(kind='bar', ax=ax, color=['#F44336','#2196F3','#4CAF50'])
ax.set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
ax.set_ylabel('Churn Rate (%)')
plt.xticks(rotation=0)
for i, v in enumerate(contract_churn):
    ax.text(i, v+0.5, f'{v:.1f}%', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('churn_by_contract.png', dpi=150)

fig2, ax2 = plt.subplots(figsize=(8,5))
feat_imp.plot(kind='barh', ax=ax2, color='#2196F3')
ax2.set_title('Top 5 Churn Predictors', fontsize=14, fontweight='bold')
ax2.invert_yaxis()
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150)

df.to_csv('churn_clean.csv', index=False)
print("\nAll files saved! Project Complete!")

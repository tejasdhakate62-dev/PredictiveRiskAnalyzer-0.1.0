import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# 1. Load data
data_path = 'master_risk_data.csv'
df = pd.read_csv(data_path)
df.columns = df.columns.str.strip()

print("🔍 Training with existing CSV columns...")

# 2. Domain Encoding
# Hum 'Title' ko hi companyName ki tarah use karenge
target_column = 'Title'
unique_domains = df[target_column].unique()
domain_map = {val: i for i, val in enumerate(unique_domains)}
domain_map['Other'] = len(domain_map)
df['Domain_Encoded'] = df[target_column].map(domain_map)

# 3. Features Map (Mapping Dashboard Inputs to your CSV Columns)
# Dashboard inputs -> Aapki CSV ke columns
features = ['Probability', 'Impact', 'Domain_Encoded'] 

# 4. Train
X = df[features]
y = df['Risk_Score']

print(f"🚀 Training with: {features}")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. Save metadata
model_data = {
    'model': model,
    'domain_map': domain_map,
    'features': features,
    'dashboard_map': {
        'budget': 'Probability',  # Temporary mapping
        'duration': 'Impact'      # Temporary mapping
    }
}

joblib.dump(model_data, 'risk_model_package.pkl')
print("🎉 Success! risk_model_package.pkl updated.")

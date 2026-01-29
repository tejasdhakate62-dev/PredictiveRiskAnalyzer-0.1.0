import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1. Load data
df = pd.read_csv('project_data_100k.csv')

# 2. Simple Encoding for 'Client_Domain'
# We'll map domains to numbers so the model can read them
domain_map = {val: i for i, val in enumerate(df['Client_Domain'].unique())}
df['Client_Domain'] = df['Client_Domain'].map(domain_map)

# 3. Define Features and Target
X = df[['Budget_INR', 'Duration_Months', 'Team_Experience_Yrs', 'Team_Size', 'Rework_Level', 'Client_Domain']]
y = df['Risk_Score']

# 4. Train
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 5. Save the model and the domain map for the app to use
joblib.dump(model, 'risk_model.pkl')
joblib.dump(domain_map, 'domain_map.pkl')

print("✅ Model and Domain Map saved!")

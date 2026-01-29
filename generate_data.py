import pandas as pd
import random

# Configuration
num_rows = 100000
domains = ['Finance', 'Healthcare', 'E-commerce', 'Education', 'Retail', 'Logistics', 'Government']

data = []

for i in range(num_rows):
    project_id = f"P{i+1:06d}"
    budget = random.randint(10000, 10000000)
    duration = random.randint(1, 60)
    experience = random.randint(1, 25)
    team_size = random.randint(2, 50)
    rework = random.randint(1, 10)
    domain = random.choice(domains)
    
    # Simple logic for synthetic risk score calculation
    # High rework + low experience + low duration/high budget = High Risk
    base_risk = (rework * 0.4) + (20 / experience) + (budget / 2000000)
    risk_score = round(min(max(base_risk, 0.5), 10.0), 1)
    
    data.append([project_id, budget, duration, experience, team_size, rework, domain, risk_score])

# Create DataFrame and Save
columns = ['Project_ID', 'Budget_INR', 'Duration_Months', 'Team_Experience_Yrs', 'Team_Size', 'Rework_Level', 'Client_Domain', 'Risk_Score']
df = pd.DataFrame(data, columns=columns)
df.to_csv('project_data_100k.csv', index=False)

print(f"✅ Success! Created project_data_100k.csv with {num_rows} rows.")

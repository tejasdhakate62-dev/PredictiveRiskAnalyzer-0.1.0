import pandas as pd
import random

# Tech project titles ki list
titles = [
    "AI Voice Assistant", "Cloud Migration", "Blockchain Wallet", 
    "Cyber Security Audit", "Neural Network Trainer", "E-commerce Platform",
    "IoT Smart Hub", "SaaS Dashboard", "Big Data Pipeline"
]

data = []
# 50,000 rows generate karne ke liye loop
for i in range(1, 50001):
    proj_title = random.choice(titles)
    # Heatmap ke hisaab se 1 se 5 ki scale
    prob = random.randint(1, 5)
    impact = random.randint(1, 5)
    score = prob * impact
    
    # Heatmap logic ke mutabiq risk levels
    if score >= 15:
        level, label = "Extreme", 4
    elif score >= 10:
        level, label = "High", 2
    elif score >= 5:
        level, label = "Medium", 1
    else:
        level, label = "Low", 0
        
    data.append([f"ID-{i:05d}", f"{proj_title} v{random.randint(1,5)}", prob, impact, score, level, label])

# DataFrame create karke CSV mein save karna
df = pd.DataFrame(data, columns=["Project_ID", "Title", "Probability", "Impact", "Risk_Score", "Category", "Label"])
df.to_csv("master_risk_data.csv", index=False)

print("Done! 'master_risk_data.csv' file aapke folder mein save ho gayi hai.")

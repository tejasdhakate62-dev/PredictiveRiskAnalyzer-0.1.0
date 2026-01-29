from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the brain
model = joblib.load('risk_model.pkl')
domain_map = joblib.load('domain_map.pkl')

@app.route('/')
def home():
    # This looks for index.html inside the 'templates' folder
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    domain_id = domain_map.get(data.get('domain'), 0)
    
    features = pd.DataFrame([{
        'Budget_INR': float(data['budget']),
        'Duration_Months': int(data['duration']),
        'Team_Experience_Yrs': int(data['experience']),
        'Team_Size': int(data.get('teamSize', 5)),
        'Rework_Level': int(data['rework']),
        'Client_Domain': domain_id
    }])

    prediction = model.predict(features)[0]
    return jsonify({'risk_score': round(float(prediction), 1)})

if __name__ == '__main__':
    app.run(debug=True)

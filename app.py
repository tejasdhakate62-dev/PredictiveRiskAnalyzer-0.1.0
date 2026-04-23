from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# --- 1. Load the brain ---
model_path = 'risk_model_package.pkl'

if os.path.exists(model_path):
    package = joblib.load(model_path)
    model = package['model']
    domain_map = package['domain_map']
    # Ye features training ke waqt use huye the
    training_features = package.get('features', []) 
    print(f"✅ AI Model loaded. Features expected: {training_features}")
else:
    print("❌ Error: 'risk_model_package.pkl' not found.")

# --- 2. Routes Setup ---

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Dashboard se aane wala naya data
        budget = float(data.get('budget', 0))
        duration = float(data.get('duration', 0))
        experience = float(data.get('experience', 1))
        team_size = float(data.get('teamSize', 1))
        rework = float(data.get('rework', 1))
        
        user_domain = data.get('companyName', 'Other')
        domain_id = domain_map.get(user_domain, domain_map.get('Other', 0))

        # --- SYNC LOGIC: Mapping Dashboard to Model Features ---
        # Agar aapka model purani CSV (Probability/Impact) par train hai:
        input_data = {}
        if 'Probability' in training_features:
            # Budget aur Rework ko Probability ki tarah treat karein
            input_data['Probability'] = (rework * 0.7) + (budget / 1000000 * 0.3)
        if 'Impact' in training_features:
            # Duration ko Impact ki tarah treat karein
            input_data['Impact'] = (duration / 12)
        if 'Domain_Encoded' in training_features:
            input_data['Domain_Encoded'] = domain_id

        # Agar model naye features par train hai (Budget_INR, etc.):
        if 'Budget_INR' in training_features: input_data['Budget_INR'] = budget
        if 'Duration_Months' in training_features: input_data['Duration_Months'] = duration
        if 'Rework_Level' in training_features: input_data['Rework_Level'] = rework

        # DataFrame banayein strictly training features ke order mein
        features_df = pd.DataFrame([input_data])
        
        # Prediction
        prediction = model.predict(features_df)[0]
        
        # --- SCORE NORMALIZATION (1-10 Range Fix) ---
        # Agar prediction 10 se upar ja rahi hai, toh use scale down karein
        final_score = float(prediction)
        if final_score > 10:
            final_score = (final_score / 100) * 10 # Example if it's 25, it becomes 2.5
            if final_score < 1: final_score = rework # Fallback to rework level
        
        return jsonify({'risk_score': round(final_score, 1)})
    
    except Exception as e:
        print(f"Prediction Error: {e}")
        # Error hone par ek smart fallback score nikalein
        fallback = (float(data.get('rework', 5)) * 0.8)
        return jsonify({'risk_score': round(fallback, 1)})

if __name__ == '__main__':
    app.run(debug=True)

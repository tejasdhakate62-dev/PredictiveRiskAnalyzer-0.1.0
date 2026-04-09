# PredictiveRiskAnalyzer 0.1.0🛡️

An end-to-end Machine Learning web application designed to predict and analyze potential risks using Python and Flask.

## 🚀 Overview
This project utilizes a trained classification model to evaluate risk factors based on user-provided data. It features a clean UI for input and provides real-time risk assessments.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Web Framework:** Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Data Handling:** Joblib/Pickle for model serialization

## 📂 Project Structure
* `app.py`: The main Flask application script.
* `train_model.py`: Script used for data preprocessing and model training.
* `risk_model.pkl`: The serialized (trained) machine learning model.
* `templates/`: HTML files for the web interface.
* `project_data_100k.csv`: Dataset used for training and validation.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tejasdhakate62-dev/PredictiveRiskAnalyzer.git](https://github.com/tejasdhakate62-dev/PredictiveRiskAnalyzer.git)
   cd PredictiveRiskAnalyzer
Run Project Commands For Linux/Ubuntu/Fedora:
* `cd ~/PredictiveRiskAnalyzer`: Navigate the project directory.
* `source venv/bin/activate`: Activate your Virtual Environment.
* `pip install flask pandas scikit-learn joblib`: Ensure all libraries are installed.
* `python3 train_model.py`: Train the model.
* `python3 app.py`: Run the server.
<img width="1920" height="1080" alt="Screenshot From 2026-01-25 21-22-34" src="https://github.com/user-attachments/assets/6552340b-0513-4d65-b0ac-0e6c2772f6c0" />
<img width="1920" height="1080" alt="Screenshot From 2026-01-26 20-44-27" src="https://github.com/user-attachments/assets/63ed7281-7f65-4830-9634-aa374737ed5b" />
<img width="1376" height="769" alt="Screenshot From 2026-01-25 22-01-17" src="https://github.com/user-attachments/assets/3020d7c4-9fee-4383-b16f-94da645e4805" />
<img width="1920" height="1080" alt="Screenshot From 2026-01-26 20-43-54" src="https://github.com/user-attachments/assets/4e847093-e2e1-434f-8c9d-89805488ba6e" />
<img width="1920" height="1080" alt="Screenshot From 2026-01-29 20-21-11" src="https://github.com/user-attachments/assets/d5fe8fbd-a15d-4718-b2e5-cce26a9a4e5f" />

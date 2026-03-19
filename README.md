# Heart-Disease-Prediction-System


## Project Overview
The **Heart Disease Prediction System** is a machine learning-based web application that predicts the likelihood of a person having heart disease based on clinical and lifestyle features. The system uses a trained machine learning model to provide predictions through a user-friendly web interface.

## Features
- Predicts the risk of heart disease using user inputs.
- Interactive and responsive web frontend built with HTML.
- Flask backend to handle user inputs and model predictions.
- Trained machine learning model saved as a pickle file for fast prediction.

## Project Structure



## Dataset
- **File:** `heart_disease_data.csv`  
- **Description:** Contains clinical and demographic features used to predict heart disease.  
- **Columns:** Age, Sex, Chest Pain Type, Resting Blood Pressure, Cholesterol, Fasting Blood Sugar, Resting ECG results, Max Heart Rate, Exercise Induced Angina, ST depression, Slope of ST segment, Number of major vessels, Thalassemia, Target (disease outcome)  

## Installation

1. **Clone the repository**


python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

python app.py

For downloading Model

import pickle

# Save the trained model
with open('heart_model.pkl', 'wb') as f:
    pickle.dump(model, f)
git clone <your-repo-url>
cd Heart_Disease_Prediction

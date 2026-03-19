from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('heart_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [
            int(request.form['age']),
            int(request.form['sex']),
            int(request.form['cp']),
            int(request.form['trestbps']),
            int(request.form['chol']),
            int(request.form['fbs']),
            int(request.form['restecg']),
            int(request.form['thalach']),
            int(request.form['exang']),
            float(request.form['oldpeak']),
            int(request.form['slope']),
            int(request.form['ca']),
            int(request.form['thal']),
        ]

        input_data = np.array(features).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]

        result = {
            'prediction': int(prediction),
            'probability_positive': round(float(probability[1]) * 100, 2),
            'probability_negative': round(float(probability[0]) * 100, 2),
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

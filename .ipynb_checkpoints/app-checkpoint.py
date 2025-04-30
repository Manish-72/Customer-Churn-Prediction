import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model
model = joblib.load('model/churn_prediction_model.pkl')

@app.route('/')
def home():
    return "✅ Customer Churn Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(input_features)
        return jsonify({'churn_prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

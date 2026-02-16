from flask import Flask, request, jsonify, send_from_directory
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the trained model
import os
model_path = os.path.join(os.path.dirname(__file__), 'air_quality_prediction.pkl')
try:
    with open("air_quality_prediction.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{model_path}' does not exist.")
    model = None

# Initialize StandardScaler with typical feature ranges from air quality data
# Features: [PM2.5, NO2, O3, CO]
# Creating a representative sample of the typical range of values
scaler = StandardScaler()
# Fit with a broader range of realistic air quality measurements
training_samples = np.array([
    [10, 20, 10, 100],      # Very good air quality
    [25, 50, 30, 200],      # Good air quality
    [50, 100, 50, 300],     # Moderate
    [100, 200, 100, 500],   # Unhealthy for sensitive
    [150, 300, 150, 700],   # Unhealthy
    [250, 500, 250, 900],   # Very unhealthy
    [400, 1200, 400, 1000], # Hazardous
])
scaler.fit(training_samples)

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/predict.html')
def predict_page():
    return send_from_directory('static', 'predict.html')

@app.route('/', methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Please ensure the model file exists."}), 500

    try:
        # Get input features from the request
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        
        # Scale features using StandardScaler (same as training)
        scaled_features = scaler.transform(features)

        # Make prediction using the loaded model
        prediction = model.predict(scaled_features)[0]

        # Provide suggestions based on AQI value
        if prediction <= 50:
            suggestion = """
                <ul>
                    <li>Good: Air quality is considered satisfactory.</li>
                    <li>Anyone can go out at any time without any issues and is pretty healthy.</li>
                    <li>Spend time outdoors and enjoy the fresh air.</li>
                    <li>Exercise and engage in physical activities.</li>
                    <li>Keep windows open and let the air circulate indoors.</li>
                </ul>
            """
        elif prediction <= 100:
            suggestion = """
                <ul>
                    <li>Moderate: Air quality is acceptable; however, some pollutants may be a concern for sensitive groups.</li>
                    <li>Sensitive groups should consider limiting prolonged outdoor exertion.</li>
                    <li>Stay hydrated to keep your lungs moist.</li>
                    <li>Avoid exercising in areas with high traffic.</li>
                </ul>
            """
        elif prediction <= 150:
            suggestion = """
                <ul>
                    <li>Unhealthy for Sensitive Groups: Members of sensitive groups may experience health effects.</li>
                    <li>They are advised not to go out during this time.</li>
                    <li>Wear masks when heading out.</li>
                    <li>Avoid intense outdoor activities.</li>
                    <li>Use air purifiers indoors if needed.</li>
                </ul>
            """
        elif prediction <= 200:
            suggestion = """
                <ul>
                    <li>Unhealthy for everyone: Everyone may begin to experience health effects like breathing issues and headaches.</li>
                    <li>Everyone should be cautious and wear masks.</li>
                    <li>Strongly encourage wearing masks and limiting outdoor activities.</li>
                    <li>Seal windows and doors with weather strips.</li>
                    <li>Keep an emergency kit ready.</li>
                </ul>
            """
        elif prediction <= 300:
            suggestion = """
                <ul>
                    <li>Very Unhealthy: Health alert: everyone may experience more serious health effects.</li>
                    <li>This range is very dangerous and may cause serious issues for everyone.</li>
                    <li>Take all necessary precautions and stay indoors.</li>
                    <li>Ensure that medication is available and ready to use.</li>
                </ul>
            """
        else:
            suggestion = """
                <ul>
                    <li>Hazardous: Health warning of emergency conditions.</li>
                    <li>The entire population is more likely to be affected.</li>
                    <li>Everyone is advised to stay indoors and avoid any outdoor activities.</li>
                    <li>Wear masks if going outside is absolutely necessary.</li>
                    <li>Keep windows and doors closed.</li>
                    <li>Create clean air zones in your home.</li>
                    <li>Seek immediate medical attention if you experience symptoms like difficulty breathing, chest pain, or headaches.</li>
                </ul>
            """

        # Return the prediction and suggestion as JSON
        return jsonify({"prediction": prediction, "suggestion": suggestion})
    except Exception as e:
        return jsonify({"error": "Invalid input. Please provide valid numeric values."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
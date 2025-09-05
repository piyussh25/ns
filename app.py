
from flask import Flask, request, jsonify, render_template
from predict_hours import predict_hours
from bulk_predict import bulk_predict
import json

app = Flask(__name__)

# Load the historical event data
with open('event_data.json', 'r') as f:
    historical_events = json.load(f)['events']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    event_name = data['event_name']
    predicted_hours, _ = predict_hours(event_name, historical_events)
    return jsonify({'predicted_hours': predicted_hours})

@app.route('/bulk_predict', methods=['POST'])
def bulk_predict_route():
    data = request.get_json()
    event_names = data['event_names']
    test_events = [{'event': name} for name in event_names]
    predictions, total_hours = bulk_predict(test_events, historical_events)
    return jsonify({'predictions': predictions, 'total_hours': total_hours})

if __name__ == '__main__':
    app.run(debug=True) # Keep debug for local development

# For production, Gunicorn will run the app


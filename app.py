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
    
    # Call bulk_predict, but we'll modify the output to exclude similar_event
    predictions_with_similar, total_hours = bulk_predict(test_events, historical_events)
    
    # Create a new list of predictions without the 'similar_event' key
    predictions_for_frontend = []
    for p in predictions_with_similar:
        predictions_for_frontend.append({
            'event': p['event'],
            'predicted_hours': p['predicted_hours']
        })
        
    return jsonify({'predictions': predictions_for_frontend, 'total_hours': total_hours})

if __name__ == '__main__':
    app.run(debug=True)
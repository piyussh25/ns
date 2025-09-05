import json
from predict_hours import predict_hours

def bulk_predict(test_events, historical_events):
    total_hours = 0
    predictions = []
    for test_event in test_events:
        predicted_hours, similar_event = predict_hours(test_event['event'], historical_events)
        predictions.append({
            'event': test_event['event'],
            'predicted_hours': predicted_hours,
            'similar_event': similar_event
        })
        total_hours += predicted_hours
    return predictions, total_hours

if __name__ == '__main__':
    # Load the historical event data
    with open('event_data.json', 'r') as f:
        historical_events = json.load(f)['events']

    # Load the test event data
    with open('test_events.json', 'r') as f:
        test_events = json.load(f)['events']

    # Perform bulk prediction
    predictions, total_hours = bulk_predict(test_events, historical_events)

    # Print the results
    print("--- Bulk Prediction Report ---")
    for prediction in predictions:
        print(f"Event: '{prediction['event']}'")
        print(f"  Predicted Hours: {prediction['predicted_hours']}")
        print(f"  Similar Event: '{prediction['similar_event']}'")
        print("---")
    print(f"Total Predicted Hours: {total_hours}")
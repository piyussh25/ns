
import json
from predict_hours import predict_hours

def evaluate_model(historical_events, current_year_events):
    total_absolute_error = 0
    num_events = len(current_year_events)
    
    print("\n--- Model Evaluation Report ---")
    print("Event | Predicted Hours | Actual Hours | Difference")
    print("--------------------------------------------------")

    for event_data in current_year_events:
        event_name = event_data['name']  # Use 'name' key for current year data
        actual_hours = event_data['working_hours']
        
        predicted_hours, similar_event = predict_hours(event_name, historical_events)
        
        difference = abs(predicted_hours - actual_hours)
        total_absolute_error += difference
        
        print(f"{event_name[:30]:<30} | {predicted_hours:<15} | {actual_hours:<12} | {difference:<10}")

    if num_events > 0:
        mae = total_absolute_error / num_events
        print("--------------------------------------------------")
        print(f"Mean Absolute Error (MAE): {mae:.2f}")
    else:
        print("No events to evaluate.")

if __name__ == '__main__':
    # Load historical event data
    with open('event_data.json', 'r') as f:
        historical_events = json.load(f)['events']

    # Load current year event data
    with open('current_year_data.json', 'r') as f:
        current_year_events = json.load(f)['events']

    evaluate_model(historical_events, current_year_events)

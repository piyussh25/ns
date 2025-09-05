
import json

def merge_data(historical_file, current_year_file):
    # Load historical data
    with open(historical_file, 'r') as f:
        historical_data = json.load(f)

    # Load current year data
    with open(current_year_file, 'r') as f:
        current_year_data = json.load(f)

    # Convert current year data to match historical data format (if necessary)
    # Assuming current_year_data has 'name' and 'working_hours'
    # and historical_data has 'event' and 'hours'
    # We need to convert 'name' to 'event' and 'working_hours' to 'hours'
    converted_current_year_events = []
    for event in current_year_data['events']:
        converted_current_year_events.append({
            'event': event['name'],
            'working_hours': event['working_hours']
        })

    # Merge the events, avoiding duplicates if an event with the exact name already exists
    # For simplicity, we'll just append for now. If strict de-duplication is needed, it's more complex.
    historical_data['events'].extend(converted_current_year_events)

    # Save the merged data back to the historical file
    with open(historical_file, 'w') as f:
        json.dump(historical_data, f, indent=2)

    print(f"Successfully merged {len(converted_current_year_events)} events from {current_year_file} into {historical_file}")

if __name__ == '__main__':
    historical_file = 'event_data.json'
    current_year_file = 'current_year_data.json'
    merge_data(historical_file, current_year_file)

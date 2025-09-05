import json
import re

def extract_event_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    all_events = []
    for page_data in data:
        content = page_data.get('content', '')
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            # Use regex to find lines that start with a number and a date
            match = re.match(r'^\d+\s+\d{1,2}\s+\w+', line)
            if match:
                parts = line.split()
                try:
                    hours = int(parts[-1])
                    event_name = ' '.join(parts[2:-1])
                    all_events.append({'event': event_name, 'hours': hours})
                except (ValueError, IndexError):
                    pass
    return all_events

def save_event_data(event_data, output_file):
    with open(output_file, 'w') as f:
        json.dump(event_data, f, indent=2)

# Specify the input and output file paths
input_json_file = 'converted (1).json'
output_json_file = 'event_data.json'

# Extract and save the event data
event_data = extract_event_data(input_json_file)
save_event_data(event_data, output_json_file)

print(f"Successfully extracted and saved {len(event_data)} events to {output_json_file}")
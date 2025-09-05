import json
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def predict_hours(new_event_name, historical_events):
    # Create a list of all event names
    all_event_names = [event['event'] for event in historical_events]
    all_event_names.append(new_event_name)

    # Vectorize the event names
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_event_names)

    # Calculate the cosine similarity between the new event and all historical events
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Get the index of the most similar event
    most_similar_event_index = cosine_similarities.argmax()

    # Get the most similar event and its working hours
    most_similar_event = historical_events[most_similar_event_index]
    predicted_hours = most_similar_event['working_hours']

    return predicted_hours, most_similar_event['event']

if __name__ == '__main__':
    # Load the historical event data
    with open('event_data.json', 'r') as f:
        historical_events = json.load(f)['events']

    # Get the new event name from the command-line arguments
    if len(sys.argv) > 1:
        new_event_name = sys.argv[1]
    else:
        print("Please provide an event name as a command-line argument.")
        sys.exit(1)

    # Predict the working hours for the new event
    predicted_hours, similar_event = predict_hours(new_event_name, historical_events)

    print(f"\nPredicted working hours for '{new_event_name}': {predicted_hours}")
    print(f"Based on the most similar event: '{similar_event}'")

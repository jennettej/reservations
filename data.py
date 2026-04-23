import json
import os

def load_reservations(filename='reservations.json'):
    """
    Load reservations from JSON file.
    Returns empty list if no file.
    """
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return []

def save_reservations(reservations, filename='reservations.json'):
    """
    Save reservations list to JSON.
    """
    with open(filename, 'w') as f:
        json.dump(reservations, f, indent=2)
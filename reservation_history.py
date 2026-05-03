import json
import os
import datetime

# Name of the JSON file where reservation history will be stored
HISTORY_FILE = "reservation_history.json"


def load_history(filename=HISTORY_FILE):
    """
    Loads all past reservation records from the history JSON file.

    Parameters:
    filename (str): Name of the history file.

    Returns:
    list: A list of past reservations.
          Returns an empty list if file does not exist or cannot be read.
    """

    # If history file does not exist yet, return empty list
    if not os.path.exists(filename):
        return []

    try:
        # Open the file in read mode
        with open(filename, "r") as file:

            # Convert JSON data into Python list
            return json.load(file)

    except:
        # If file is corrupted or empty, return empty list
        return []


def save_history(history, filename=HISTORY_FILE):
    """
    Saves reservation history back into the JSON file.

    Parameters:
    history (list): Updated list of historical reservations.
    filename (str): Name of the history file.
    """

    # Open file in write mode (creates file if it does not exist)
    with open(filename, "w") as file:

        # Save Python list into JSON format with indentation for readability
        json.dump(history, file, indent=4)


def add_to_history(reservation, action):
    """
    Adds a reservation to history after it is checked out or canceled.

    Parameters:
    reservation (dict): Reservation being archived.
    action (str): Type of action performed.
                  Examples:
                  - "Checked Out"
                  - "Canceled"
    """

    # Load current reservation history
    history = load_history()

    # Make a copy so original reservation data is not altered
    reservation_copy = reservation.copy()

    # Add the action performed
    reservation_copy["historyAction"] = action

    # Add today's date as the date it was archived
    reservation_copy["historyDate"] = datetime.date.today().strftime("%m-%d-%Y")

    # Add updated reservation record into history list
    history.append(reservation_copy)

    # Save updated history back into file
    save_history(history)


def view_history():
    """
    Displays all stored reservation history records.

    Returns:
    str:
        "No reservation history found." if no records exist.
        "" after printing history successfully.
    """

    # Load all reservation history
    history = load_history()

    # If no records exist
    if not history:
        return "No reservation history found."

    # Display section title
    print("\n--- Reservation History ---")

    # Loop through every archived reservation
    for reservation in history:

        # Divider for readability
        print("--------------------------------")

        # Print guest full name
        print(f"Guest: {reservation['firstName']} {reservation['lastName']}")

        # Print confirmation number
        print(f"Confirmation #: {reservation['confirmationNumber']}")

        # Print room number
        print(f"Room #: {reservation['roomNumber']}")

        # Print stay dates
        print(f"Arrival Date: {reservation['arrivalDate']}")
        print(f"Departure Date: {reservation['leaveDate']}")

        # Print why reservation was archived
        print(f"Action: {reservation['historyAction']}")

        # Print when reservation was archived
        print(f"History Date: {reservation['historyDate']}")

    # Return empty string so function completes cleanly
    return ""
# Author: Jonathan Miller
# This file contains functions for converting dates and closing reservations.

import datetime
from reservation_history import add_to_history


def mmddyyyy_to_date(text):
    '''
    Convert a date string in the format "MM-DD-YYYY" to a datetime.date object.
    '''
    return datetime.datetime.strptime(text, "%m-%d-%Y").date()


def date_to_mmddyyyy(date):
    '''
    Convert a datetime.date object to a string in the format "MM-DD-YYYY".
    '''
    return date.strftime("%m-%d-%Y")


def close_reservation(reservations, confirmation_number):
    """
    Move a reservation to history, then remove it from current reservations.
    """
    for reservation in reservations:
        if reservation.get("confirmationNumber") == confirmation_number:
            add_to_history(reservation, "Checked Out")
            reservations.remove(reservation)
            return "Reservation closed and moved to history."

    return "Reservation not found."


def validate_existing_confirm_num(confirm_num, reservations):
    """
    Validates confirmation number is a positive integer and exists in reservations.
    """
    try:
        val = int(confirm_num)

        if val < 1:
            raise ValueError

    except ValueError:
        raise ValueError("Confirmation number must be a positive integer.")

    for res in reservations:
        if val == res["confirmationNumber"]:
            return val

    raise ValueError("Confirmation number not found.")


def close_reservation_cli(self):
    """
    Closes a reservation selected by confirmation number.
    """
    from data import load_reservations, save_reservations
    from edit import read_reservations, read_reservation

    while True:
        reservations = load_reservations(self.filename)

        if not reservations:
            return "No reservations found"

        read_reservations(self)

        user_in = input("\nConfirmation number to close or [S]kip: ").strip()

        if user_in.lower() == 's':
            return "No reservations closed."

        try:
            confirmation_number = validate_existing_confirm_num(user_in, reservations)

        except ValueError as err:
            print(err)
            continue

        for res in reservations:
            if confirmation_number == res["confirmationNumber"]:
                read_reservation(res)

                while True:
                    close_in = input("Close this reservation? [Y]es or [N]o: ").strip()

                    if close_in.lower() == 'y':
                        latest_reservations = load_reservations(self.filename)

                        still_exists = any(
                            r.get("confirmationNumber") == confirmation_number
                            for r in latest_reservations
                        )

                        if not still_exists:
                            return "Reservation was already closed by another session."

                        message = close_reservation(latest_reservations, confirmation_number)
                        save_reservations(latest_reservations, self.filename)

                        return message

                    elif close_in.lower() == 'n':
                        return "No reservations closed."

                    else:
                        print("Invalid option. Please enter 'Y' or 'N'.")
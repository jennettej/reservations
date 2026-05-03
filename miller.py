# Author: Jonathan Miller
# This file contains functions for converting dates and closing reservations.

import datetime

def mmddyyyy_to_date(text):
    '''
    Convert a date string in the format "MM-DD-YYYY" to a datetime.date object.
    Parameters:
    text (str): A date string in the format "MM-DD-YYYY".
    Returns:
    datetime.date: A date object containing the converted input date.
    '''
    return datetime.datetime.strptime(text, "%m-%d-%Y").date()

def date_to_mmddyyyy(date):
    '''
    Convert a datetime.date object to a string in the format "MM-DD-YYYY".
    Parameters:
    date (datetime.date): A date object.
    Returns:
    str: A date string in the format "MM-DD-YYYY".
    '''
    return date.strftime("%m-%d-%Y")

def close_reservation(reservations, confirmation_number):
    '''
    Remove a reservation by confirmation number.
    Modifies list in place.
    '''
    reservations[:] = [r for r in reservations if r.get('confirmationNumber') != confirmation_number]

def validate_existing_confirm_num(confirm_num, reservations):
    """
    Validates confirmation number is a positive integer and exists in reservations.
    @param confirm_num: confirmation number
    @param reservations: list of reservations
    @return: confirmation number if valid
    """
    try:
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
    except ValueError as err:
        raise err

def close_reservation_cli(self):
    """
    Closes (removes) a reservation selected by confirmation number.
    """
    from data import load_reservations, save_reservations
    from edit import read_reservations, read_reservation

    while 1:
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
                while 1:
                    close_in = input("Close this reservation? [Y]es or [N]o: ").strip()
                    if close_in.lower() == 'y':
                        latest_reservations = load_reservations(self.filename)
                        still_exists = any(
                            r.get("confirmationNumber") == confirmation_number
                            for r in latest_reservations
                        )
                        if not still_exists:
                            return "Reservation was already closed by another session."
                        close_reservation(latest_reservations, confirmation_number)
                        save_reservations(latest_reservations, self.filename)
                        return "Closed reservation successfully."
                    elif close_in.lower() == 'n':
                        return "No reservations closed."
                    else:
                        print("Invalid option. Please enter 'Y' or 'N'.")
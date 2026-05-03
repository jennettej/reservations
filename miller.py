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

from reservation_history import add_to_history

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

if __name__ == "__main__":
    main()

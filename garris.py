import datetime
#Rush Garris

def days_between(date1:datetime.date, date2:datetime.date) -> int:
    '''
    Calculate the number of days between 2 dates.

    Params: 
    date1: the first date.
    date2: the second date.

    Returns:
    int: the absolute difference between the two days.
    '''
    diff = date1 - date2
    return abs(diff.days)


def validate_date(date_str: str):
    '''
    Validates a date string in the format "MM/DD/YYYY".

    Args:
        date_str: The date string to validate.):

    '''
    try:
        parsed_date = datetime.datetime.strptime(date_str, "%m/%d/%Y").date()
        return parsed_date
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}. Expected MM/DD/YYYY.")

def check_availability(room_number: int, checkin: datetime.date, checkout: datetime.date, reservations: list):
    '''
    Check if a room is available for the requested date range.

    Params:
    room_number: the room number to check (1-8).
    checkin: the requested check-in date.
    checkout: the requested check-out date.
    reservations: a list of existing reservations, each a dict with keys
                  'room_number' (int), 'checkin' (datetime.date), 'checkout' (datetime.date).

    Returns:
    bool: True if the room is available, False if it is already booked.
    '''
    for reservation in reservations:
        if reservation['room_number'] == room_number:
            if reservation['checkin'] < checkout and checkin < reservation['checkout']:
                return False
    return True

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


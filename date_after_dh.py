# Take input, start date and duration in days, return datetime.date object
# Started by David Holladay on March 18th, 2026
import datetime

def date_after(start_date: str, duration_days: int) -> datetime.date:
    '''
Takes a string input as a date, format MM/DD/YYYY, and the number of days, as a int. Returns datetime object
    '''
    
    start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y")

    end_date = start_date + datetime.timedelta(days=duration_days)

    return end_date
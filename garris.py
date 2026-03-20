import datetime

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

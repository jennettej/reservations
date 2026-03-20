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

def main():
    '''
    Main function to test and showcase the date conversion functions. No other use.
    '''
    test1_input = "06-01-2024"
    test2_input = "08-07-2024"

    test_date = mmddyyyy_to_date(test1_input)
    test2_date = mmddyyyy_to_date(test2_input)

    print(date_to_mmddyyyy(test_date))
    print(date_to_mmddyyyy(test2_date))


if __name__ == "__main__":
    main()

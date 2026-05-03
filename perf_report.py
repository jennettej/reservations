import json
import datetime
import miller
from data import load_reservations
from edit import read_reservation 

def performance_report():
    """reads the file with the current reservations and returns the number of reservations
        as well as lists the reservations that are being requested."""

    res_file = load_reservations()
    try:
        month_request = input(f'What month and year would you like your report from (mm-yyyy)? ')
        (req_month, req_year) = month_request.split('-')
        if int(req_month) < 1 or int(req_month) > 12 or int(req_year) < 0:
            raise ValueError


        active_reservations = 0
        

        for r in res_file:
            arrival_date = miller.mmddyyyy_to_date(r['arrivalDate'])
            leave_date = miller.mmddyyyy_to_date(r['leaveDate']) 

            if (arrival_date.year, arrival_date.month) <= (int(req_year), int(req_month)) <= (leave_date.year, leave_date.month):

                read_reservation(r)
                active_reservations += 1 
        if active_reservations == 0:
            print()
            print('There are no reservations for this month.')
        else:
            print()
            print(f'Number of reservations: {active_reservations}')
        return len(res_file), res_file

    except:
        print('Invalid input. Must be in the format mm-yyyy and a valid month and year')

def date_trends():
    """
    - Creates a list sorted by start month
    - Returns a dictionary where if creats a frequeuncy of how many
      reservations are in each month
    - Frequeuncy increases for every time a reservation includes the same
      date and year
    """
    res_file = load_reservations()
    lst = []
    freq_dic = {}

    for reservations in res_file:
        arrival_date = miller.mmddyyyy_to_date(reservations['arrivalDate'])
        leave_date = miller.mmddyyyy_to_date(reservations['leaveDate'])
        lst.append([arrival_date, leave_date, (leave_date - arrival_date).days])
    

        curr_month = arrival_date.month 
        curr_year = arrival_date.year 
        lst_month = leave_date.month
        lst_year = leave_date.year

        while (curr_year, curr_month) <= (lst_year, lst_month):
            freq_dic[f'{curr_month}-{curr_year}'] = freq_dic.get(f'{curr_month}-{curr_year}', 0) + 1
            if curr_month == 12:
                curr_year += 1
                curr_month = 1

            else:
                curr_month += 1
    sorted_lst = sorted(lst, key=lambda x: x[0])
    return freq_dic

def display_frequency_report():
    """returns a formatted version of the frequencies of each date-month from date_trends function"""
    freq_dic = date_trends()
    print('| Month  | Frequency | ')
    for month in freq_dic:
        print('|', month, '|', " " * (8 - len(str(freq_dic[month]))), freq_dic[month], '|')

    return 


            

def main():
    choice = input('1: Performance Report\n2: Frequency Report\nChoice: ')
    if choice == '1':
        performance_report()
    elif choice == '2':
        display_frequency_report()

if __name__ == "__main__":
    main()

    


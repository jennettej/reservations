import json
import datetime 

def performance_report():
    '''reads the file with the current reservations and returns the number of reservations
        and also lists the reservations that are currently reported.'''
    with open('reservations.json', 'r') as filename:

        res_file = json.load(filename)

    return len(res_file), res_file

def date_trends():
    '''
    - Creates a list sorted by start month
    - Returns a dictionary where if creats a frequeuncy of how many
      reservations are in each month
    - Frequeuncy increases for every time a reservation includes the same
      date and year
    '''
    with open('reservations.json', 'r') as filename:
        lst = []
        freq_dic = {}
        res_file = json.load(filename)

        for reservations in res_file:
            arrivalDate = datetime.datetime.strptime(reservations['arrivalDate'], '%m-%d-%Y').date()
            leaveDate = datetime.datetime.strptime(reservations['leaveDate'], '%m-%d-%Y').date()
            lst.append([arrivalDate, leaveDate, (leaveDate - arrivalDate).days])
        

            curr_month = arrivalDate.month 
            curr_year = arrivalDate.year 
            lst_month = leaveDate.month
            lst_year = leaveDate.year

            while (curr_year, curr_month) <= (leaveDate.year, leaveDate.month):
                freq_dic[f'{curr_month}-{curr_year}'] = freq_dic.get(f'{curr_month}-{curr_year}', 0) + 1
                if curr_month == 12:
                    curr_year += 1
                    curr_month = 1

                else:
                    curr_month += 1
    sorted_lst = sorted(lst, key=lambda x: x[0])
    return sorted_lst, freq_dic




            

def main():
    active, reservations = performance_report()
    print(active)
    for i in reservations:
        print(i)
    sorted_lst, freq_dic = date_trends()
    print(sorted_lst)
    print()
    print(freq_dic)


main()

    


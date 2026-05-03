import json
import datetime 

def performance_report():
    '''reads the file with the current reservations and returns the number of reservations
        and also lists the reservations that are currently reported.'''
    with open('reservations.json', 'r') as filename:

        res_file = json.load(filename)

    return len(res_file), res_file

def date_trends():
    with open('reservations.json', 'r') as filename:
        lst = []
        res_file = json.load(filename)
        for reservations in res_file:
            arrivalDate = datetime.datetime.strptime(reservations['arrivalDate'], '%m-%d-%Y').date()
            leaveDate = datetime.datetime.strptime(reservations['leaveDate'], '%m-%d-%Y').date()
            lst.append([arrivalDate, leaveDate, (leaveDate - arrivalDate).days])
            
            
            

def main():
    active, reservations = performance_report()
    print(active)
    for i in reservations:
        print(i)


main()

    


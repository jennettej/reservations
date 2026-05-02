import json

def performance_report():
    '''reads the file with the current reservations and returns the number of reservations
        and also lists the reservations that are currently reported.'''
    with open('reservations.json', 'r') as filename:

        res_file = json.load(filename)

    return len(res_file), res_file

def main():
    active, reservations = performance_report()
    print(active)
    for i in reservations:
        print(i)


main()

    


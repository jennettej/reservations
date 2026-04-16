#from datetime import datetime
import miller   # Need function to change string to datetime.date object


#Ready to commit
"""
---------------------------------------------------------------
SENG 201 - Term Project
---------------------------------------------------------------
This program avilability.py is a reservation input program to
identify the name of the guest, the date of there stay and there
date that they are leaving. It also asks for room number which is
holds information about prices, capacity, room name, and beds. This
program calculates things like total costs, length of stay, and number
of reservations put in per loop.
"""
avail = {'1': 'available', '2': 'available', '3': 'available', '4': 'available', '5': 'available', '6': 'available', '7': 'available', '8': 'available'}

def enter_name():
    '''
    -Asks user to input the guest name. Will keep asking until parameters are met. 
    -Only letters and the hyphen and apostrophe symbols are allowed. 
    -Spaces are allowed.
    '''
    is_accepted = 'false'
    while is_accepted == 'false':
        first_name = input('Please enter the first name of the guest: ')
        last_name = input('Please enter the last name of the guest: ')
        for char in first_name:
            if not char.isalpha():
                if char != "'" and char != "=" and char != " ":
                    print('Invalid name: name should be a letter and only hyphens and apostrophes are allowed')
                    continue
        is_accepted = 'true'
    full_name = f'{first_name} {last_name}'
    return full_name


def date():

    '''Asks user what day you want your reservation to be on'''
    while True:
        checkin = miller.mmddyyyy_to_date(input('Please enter your check in date (MM-DD-YYYY): '))   
        try:
            break

        except ValueError as e:
            print(f'Error: {e}')

        except Exception:
            print('An unexpected error has occured')
    while True:
        checkout = miller.mmddyyyy_to_date(input('Please enter your checkout date (MM-DD-YYYY): '))
            
        try:
            break

        except ValueError as e:
            print(f'Error: {e}')

        except Exception:
            print('An unexpected error has occured')
    while True:
        
        try:
            stay = checkout - checkin
            break

        except ValueError as e:
            print('Must be an integer')
            continue
        except Exception:
            print('An unexpected error has occured')
            continue
        
    return checkin, checkout, stay



def room():
    '''Asks user what room they want to reserve'''

    room_request = input('What room would you like to reserve?(1-8)  ')

    if room_request == '1':
        beds = '1 full'
        occupency = 2
        cost = 77
        name = 'Sea Oat Suite'

        avail['1'] = 'unavailable'

        return cost
    elif room_request =='2':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shipwreck Suite'

        avail['2'] = 'unavailable' 

        return cost
    elif room_request == '3':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shady Oak Suite'

        avail['3'] = 'unavailable' 

        return cost
    elif room_request == '4':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Sunset Suite'

        avail['4'] = 'unavailable'

        return cost
    elif room_request == '5':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Shelling Suite'

        avail['5'] = 'unavailable' 

        return cost
    elif room_request == '6':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Skipper Suite'

        avail['6'] = 'unavailable'

        return cost
    elif room_request == '7':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Salt Marsh'

        avail['7'] = 'unavailable' 

        return cost
    elif room_request == '8':
        beds = '1 king 1 queen'
        occupency = 4
        cost = 129
        name = 'Captains Quarters Apartment'

        avail['8'] = 'unavailable'

        return cost
    else:
        return 'Invalid room number'

        

        #def close_reservation():
        #close = input(f'What room would you like to close? ')
        #if room == '1':
            




def main():

    """
    Main entry point for the program.
    """
    reservations = 0
    proceed = ''
    while proceed != 'N' and proceed != 'n':
        for key, value in avail.items():
            print(f'Room Number {key} is {value}')
        name = enter_name()
        checkin, checkout, stay = date()
        cost = (room() * stay.days)
        reservations += 1
        print(reservations)
        print(f'Name: {name} \n Checkin Date: {miller.date_to_mmddyyyy(checkin)} \n Checkout Date: {miller.date_to_mmddyyyy(checkout)} \n Stay Length: {stay.days} days \n Total Cost: ${cost}')
        proceed = input('Do you wish to proceed? (Press any button to continue, or N to stop) ') 

    # TODO: Implement program logic here
    pass


if __name__ == "__main__":
    
    main()

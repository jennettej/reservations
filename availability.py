#from datetime import datetime
import miller   # Need function to change string to datetime.date object

#Ready to commit
"""
SENG 201 - Term Project
Starter Script

Description:
    TODO: Describe what this program/module is supposed to do.
    TODO: Hand avail info to JSON / database / longterm storage
    TODO: Change miller.py or avalibility.py formating for DD-MM-YYYY or DD/MM/YYYY formating
    TODO: Change stay value to int from datetime object


"""
avail = {'1': 'available', '2': 'available', '3': 'available', '4': 'available', '5': 'available', '6': 'available', '7': 'available', '8': 'available'}
checkin_object = ''
checkout_object = ''


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
        name = 'Sea Oat Sweet'

        avail['1'] = 'unavailable'

        return cost
    elif room_request =='2':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shipwreck Sweet'

        avail['2'] = 'unavailable' 

        return cost
    elif room_request == '3':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shady Oak Sweet'

        avail['3'] = 'unavailable' 

        return cost
    elif room_request == '4':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Sunset Sweet'

        avail['4'] = 'unavailable'

        return cost
    elif room_request == '5':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Shelling Sweet'

        avail['5'] = 'unavailable' 

        return cost
    elif room_request == '6':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Skipper Sweet'

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
        checkin, checkout, stay = date()
        print(miller.date_to_mmddyyyy(checkin))
        print(miller.date_to_mmddyyyy(checkout))
        cost = (room() * stay)
        print(f'${cost}')
        reservations += 1
        print(reservations)
        proceed = input('Do you wish to proceed? (Press any button to continue, or N to stop) ') 

    # TODO: Implement program logic here
    pass


if __name__ == "__main__":
    
    main()

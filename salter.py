#from datetime import datetime

#Ready to commit
"""
SENG 201 - Term Project
Starter Script

Description:
    TODO: Describe what this program/module is supposed to do.


"""
avail = {'1': 'available', '2': 'available', '3': 'available', '4': 'available', '5': 'available', '6': 'available', '7': 'available', '8': 'available'}
checkin_object = ''
checkout_object = ''


def date():
    '''Asks user what day you want your reservation to be on'''
    checkin = input('Please enter your check in date (MM/DD/YYYY): ')
    checkout = input('Please enter your checkout date (MM/DD/YYYY): ')
    stay = int(input('How many days would you like to stay for? '))
    #checkin_object = datetime.strptime(checkin, '%m/%d/%Y')
    #checkout_object = datetime.strptime(checkout, '%m/%d/%Y')
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
    while proceed != 'N':
        for key, value in avail.items():
            print(f'Room Number {key} is {value}')
        checkin, checkout, stay = date()
        print(checkin)
        print(checkout)
        cost = (room() * stay)
        print(f'${cost}')
        reservations += 1
        print(reservations)
        proceed = input('Do you wish to proceed? (Press any button to continue, or N to stop) ') 

    # TODO: Implement program logic here
    pass


if __name__ == "__main__":
    
    main()

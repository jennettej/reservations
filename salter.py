from datetime import datetime


"""
SENG 201 - Term Project
Starter Script

Description:
    TODO: Describe what this program/module is supposed to do.


"""
checkin_object = ''
checkout_object = ''
def date():
    '''Asks user what day you want your reservation to be on'''
    checkin = input('Please enter your check in date (MM/DD/YYYY): ')
    checkout = input('Please enter your checkout date (MM/DD/YYYY): ')
    checkin_object = datetime.strptime(checkin, '%m/%d/%Y')
    checkout_object = datetime.strptime(checkout, '%m/%d/%Y')
    return checkin_object, checkout_object



def room():
    '''Asks user what room they want to reserve'''
    room_request = input('What room would you like to reserve? ')
    if room_request == '1':
        beds = '1 full'
        occupency = 2
        cost = 77
        name = 'Sea Oat Sweet'

    elif room_request =='2':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shipwreck Sweet'

    elif room_request == '3':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shady Oak Sweet'

    elif room_request == '4':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Sunset Sweet'

    elif room_request == '5':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Shelling Sweet'

    elif room_request == '6':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Skipper Sweet'

    elif room_request == '7':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Salt Marsh'

    elif room_request == '8'
        beds = '1 king 1 queen'
        occupency = 4
        cost = 129
        name = 'Captains Quarters Apartment'

    else:
        return 'Invalid room number'





 main():
    """
    Main entry point for the program.
    """
    checkin, checkout = date()
    print(checkin)
    print(checkout)
    # TODO: Implement program logic here
    pass


if __name__ == "__main__":
    main()

#from datetime import datetime


"""
SENG 201 - Term Project
Starter Script

Description:
    TODO: Describe what this program/module is supposed to do.


"""
avail = ['1', '2', '3', '4', '5', '6', '7', '8']
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
        return cost, room_request
    elif room_request =='2':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shipwreck Sweet'
        return cost, room_request
    elif room_request == '3':
        beds = '2 full'
        occupency = 4
        cost = 85
        name = 'Shady Oak Sweet'
        return cost, room_request
    elif room_request == '4':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Sunset Sweet'
        return cost, room_request
    elif room_request == '5':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Shelling Sweet'
        return cost, room_request
    elif room_request == '6':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Skipper Sweet'
        return cost, room_request
    elif room_request == '7':
        beds = '1 queen'
        occupency = 2
        cost = 97
        name = 'Salt Marsh'
        return cost, room_request
    elif room_request == '8':
        beds = '1 king 1 queen'
        occupency = 4
        cost = 129
        name = 'Captains Quarters Apartment'
        return cost, room_request
    else:
        return 'Invalid room number'






def main():
    """
    Main entry point for the program.
    """
    checkin, checkout, stay = date()
    print(checkin)
    print(checkout)
    cost, room_request = (room() * stay), room_request
    print(f'${cost}')
    print(room_request)

    # TODO: Implement program logic here
    pass


if __name__ == "__main__":
    main()

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





def main():
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

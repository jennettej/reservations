"""
SENG 201 - Term Project
Starter Script

Description:
    This program serves as the welcome menus to the reservation system.
    Including:
        Housekeeping menu
        Hotel Management menu
        Clerk Services menu

"""
import os


class Welcome_Screen:
    def welcome_screen(self):
        print("Welcome to _______'s Room Reservation System" + '\n')
        print("Please Enter Your Positions Login to Access the Correct Menu." + '\n')
        print("For Hotel Management, Enter: htmn")
        print("For Housekeeping, Enter: hskp")
        print("For Clerk Services, Enter: cksv" + '\n')

        login_info = input("Enter Login Passkey Here: ")

        while True:

            if login_info == 'htmn':
                print('\n' + "Login Successful! Entering the Hotel Management Menu System...")
                next_class = Hotel_Management('reservations.txt') #Placeholder name for reservation file
                return next_class

            elif login_info == 'hskp':
                print('\n' + "Login Successful! Entering the Housekeeping Management Menu System...")
                next_class = Housekeeping('room_status.txt') #Placeholder name for file with room info
                return next_class

            elif login_info == 'cksv':
                print('\n' + "Login Successful! Entering into the Clerk Services Management Menu System...")
                next_class = Clerk_Services('reservations.txt')
                return next_class


            else:
                print('\n' + "Login Requirements Not Met, Please Try Again.")


class Clerk_Services:
    def __init__(self, filename):
        self.filename = filename

    def welcome(self):
        print("..." + '\n' + ".." + '\n' + "." + '\n')
        print("Welcome to the Clerk Services Menu...")
        print('\n' + "Below is a list of all hotel rooms:" + '\n')
        print("| Room # | Beds           | Occupancy | Cost    | Name                        |")
        print("|   1    | 1 Full         |     2     |   $77   | Sea Oat Suite               |")
        print("|   2    | 2 Full         |     4     |   $85   | Shipwreck Suite             |")
        print("|   3    | 2 Full         |     4     |   $85   | Shady Oak Suite             |")
        print("|   4    | 1 Queen        |     2     |   $97   | Sunset Suite                |")
        print("|   5    | 1 Queen        |     2     |   $97   | Shelling Suite              |")
        print("|   6    | 1 Queen        |     2     |   $97   | Skipper Suite               |")
        print("|   7    | 1 Queen        |     2     |   $97   | Salt Marsh                  |")
        print("|   8    | 1 King 1 Queen |     4     |   $129  | Captains Quarters Apartment |")

    def read_reservations(self, filename):
        print("Below is a list of current reservations:" + '\n')
        if not os.path.exists(filename):
            return "No reservations found - file does not exist"

        if os.path.getsize(filename) == 0:
            return "No reservations found - file is empty"

        with open(filename, 'r') as file:
            reservations = file.read().strip()

        return reservations

    def add_reservation(self, filename):
        print('\n' + "If you would like to create a reservation, do so here. If not enter 'skip'.")
        reservation_info = input('\n' + "Add reservation here: ")

        if reservation_info == 'skip':
            return "Skipping Reservation Creation"

        else:

            with open(self.filename, 'a') as file:
                file.write('\n' + reservation_info)

            return "Reservation Added Successfully!"


class Hotel_Management:
    def __init__(self, filename):
        self.filename = filename

    def welcome(self):
        print("..." + '\n' + ".." + '\n' + "." + '\n')
        return "Welcome to the Hotel Management Menu..."

    def read_reservations(self, filename):
        print('\n' + "Below is a list of current reservations:" + '\n')
        if not os.path.exists(filename):
            return "No reservations found - file does not exist"

        if os.path.getsize(filename) == 0:
            return "No reservations found - file is empty"

        with open(filename, 'r') as file:
            reservations = file.read().strip()

        return reservations

    def add_reservation(self, filename):
        print('\n' + "If you would like to create a reservation, do so here. If not enter 'skip'.")
        reservation_info = input('\n' + "Add reservation here: ")

        if reservation_info == 'skip':
            return "Skipping Reservation Creation"

        else:

            with open(self.filename, 'a') as file:
                file.write('\n' + reservation_info)

            return "Reservation Added Successfully!"

class Housekeeping:
    def __init__(self, filename):
        self.filename = filename

    def welcome(self):
        print("..." + '\n' + ".." + '\n' + "." + '\n')
        return "Welcome to the Housekeeping menu..."

    def room_status(self, filename):
        print('\n' + "Here is a list of each room and its current status:" + '\n')
        if not os.path.exists(filename):
            return "No rooms found - file does not exist"

        if os.path.getsize(filename) == 0:
            return "No rooms found - file is empty"

        with open(filename, 'r') as file:
            rooms = file.read().strip()

        return rooms








def main():
    """
    Main entry point for the program.
    """
    welcome = Welcome_Screen()
    hotel = Hotel_Management('reservations.txt')
    next_class = welcome.welcome_screen()
    if isinstance(next_class, Clerk_Services):
        next_class.welcome()
        print(next_class.read_reservations('reservations.txt'))
        print(next_class.add_reservation('reservations.txt'))

    elif isinstance(next_class, Hotel_Management):
        print(next_class.welcome())
        print(next_class.read_reservations('reservations.txt'))
        print(next_class.add_reservation('reservations.txt'))

    elif isinstance(next_class, Housekeeping):
        print(next_class.welcome())
        print(next_class.room_status('room_status.txt'))




   # pass


if __name__ == "__main__":
    main()

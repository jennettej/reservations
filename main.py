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
import datetime
import json
from data import load_reservations, save_reservations
from garris import check_availability, validate_date
from ReservationSearch import ReservationSearch

RESERVATIONS_FILE = 'reservations.json'
ROOM_STATUS_FILE = 'room_status.txt'



class Welcome_Screen:
    def welcome_screen(self):
        """
        The welcome_screen function serves as an opening menu to the reservation system,
        it welcomes the user and receives input that determines which of the three menus
        will be prompted next.
        """
        print("Welcome to _______'s Room Reservation System" + '\n')
        print("Please Enter Your Positions Login to Access the Correct Menu." + '\n')
        print("For Hotel [M]anagement, Enter: m")
        print("For [H]ousekeeping, Enter: h")
        print("For [C]lerk Services, Enter: c")
        print("To [Q]uit, Enter: q" + '\n')

        while True:
            login_info = input("Enter option here: ")

            # These if statements take in a "key" that determines which of the three avaliable
            # menus the program will run next.

            if login_info == 'm' or login_info == 'M':
                print('\n' + "Entering the Hotel Management Menu System...")
                next_class = Hotel_Management(RESERVATIONS_FILE) 
                return next_class

            elif login_info == 'h' or login_info == 'H':
                print('\n' + "Entering the Housekeeping Management Menu System...")
                next_class = Housekeeping(ROOM_STATUS_FILE)
                return next_class

            elif login_info == 'c' or login_info == 'C':
                print('\n' + "Entering into the Clerk Services Management Menu System...")
                next_class = Clerk_Services(RESERVATIONS_FILE)
                return next_class

            elif login_info == 'q' or login_info =='Q':
                print('\n' + "Closing program ...")
                next_class = "quit"
                return next_class

            else:
                print('\n' + "Login Requirements Not Met, Please Try Again.")
                print("Enter Hotel [M]anagement, [H]ousekeeping, [C]lerk Services, or [Q]uit" + '\n')


class Clerk_Services:
    def __init__(self, filename):
        """
        Initiates the class.
        """
        self.filename = filename

    def welcome(self):
        """
        The welcome function welcomes the user to the Clerk Services Menu and provides a
        diagram of all rooms offered at the hotel.
        """
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

    def read_reservations(self):
        """
        The read_reservations function takes in a file, determines if it exists and
        returns the reservations currently housed inside the file if there are any.
        """
        res = load_reservations(self.filename)
        if not res:
            return "No reservations found"
        for r in res:
            print(r)
        return ""

    def add_reservation(self):
        """
        The add_reservation function prompts the user to make a new reservation or skip to the next screen,
        the reservation is added to the list of the other current reservations.
        """
        print("Enter guest details (name, arrival MM/DD/YYYY, leave MM/DD/YYYY, room):")
        name = input("Name: ")
        arrival = validate_date(input("Arrival: "))
        leave = validate_date(input("Leave: "))
        room = int(input("Room (1-8): "))
        res = load_reservations(self.filename)
        res.append({"name": name, "arrival": arrival.strftime("%m/%d/%Y"), "leave": leave.strftime("%m/%d/%Y"), "room": room})
        save_reservations(res, self.filename)
        return "Reservation added and saved."
    
    def class_option(self):
        '''
        Asks user option to book a reservation, show reservations, quit, show menu, or exit user.
        '''
        while True:
            option = input("[B]ook reservation, [S]how reservations, [Q]uit program, [E]xit user: ")
            if option == "B" or option == "b":
                return "book"
            elif option == 'S' or option == 's':
                return "show"
            elif option == 'Q' or option == 'q':
                return "quit"
            elif option == 'E' or option == 'e':
                return "exit"
            elif option == 'M' or option == 'm':
                return "menu"
            else:
                print("Invalid optoin, enter 'B' to book, 'S' to show reservations, 'Q' to quit, or 'E' to exit")







class Hotel_Management:
    def __init__(self, filename):
        """
        Initiates the class.
        """
        self.filename = filename

    def welcome(self):
        """
        The welcome function welcomes the user to the Hotel Management Menu.
        """
        print("..." + '\n' + ".." + '\n' + "." + '\n')
        return "Welcome to the Hotel Management Menu..."

    def read_reservations(self):
        """
        The read_reservations function takes in a file, determines if it exists and
        returns the reservations currently housed inside the file if there are any.
        """
        res = load_reservations(self.filename)
        if not res:
            return "No reservations found"
        for r in res:
            print(r)
        return ""

    def add_reservation(self):
        """
        The add_reservation function prompts the user to make a new reservation or skip to the next screen,
        the reservation is added to the list of the other current reservations.
        """
        print('\n' + "If you would like to create a reservation, do so here. If not enter 's' to [s]kip'.")
        reservation_info = input('\n' + "Add reservation here: ")

        if reservation_info == 'skip' or reservation_info == 's' or reservation_info == 'S':
            # Allows for the user to skip adding a reservation
            return "Skipping Reservation Creation"

        else:

            with open(self.filename, 'a') as file:
                # Adds a reservation to the file
                file.write('\n' + reservation_info)

            return "Reservation Added Successfully!"
    
    def class_option(self):
        '''
        Asks user option to read reservations, book reservations, quit, or exit user.
        '''
        while True:
            option = input("[B]ook reservation, [S]how reservations, [Q]uit program, [E]xit user: ")
            if option == "B" or option == "b":
                return "book"
            elif option == 'S' or option == 's':
                return "show"
            elif option == 'Q' or option == 'q':
                return "quit"
            elif option == 'E' or option == 'e':
                return "exit"
            else:
                print("Invalid optoin, enter 'B' to book, 'S' to show reservations, 'Q' to quit, or 'E' to exit")        


class Housekeeping:
    def __init__(self, filename):
        """
        Initiates the class. Creates room_status.txt with all rooms defaulting
        to 'clean' if the file does not already exist.
        """
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                for room_num in range(1, 9):
                    file.write(f"Room {room_num}: clean\n")

    def welcome(self):
        """
        The welcome function welcomes the user to the Housekeeping Menu.
        """
        print("..." + '\n' + ".." + '\n' + "." + '\n')
        return "Welcome to the Housekeeping menu..."

    def room_status(self, filename):
        """
        The room_status function intakes a file, checks if it exists, and returns
        the list of rooms in the hotel and their current status.
        """
        print('\n' + "Here is a list of each room and its current status:" + '\n')
        if not os.path.exists(filename):
            # Checks if the file exists
            return "No rooms found - file does not exist"

        if os.path.getsize(filename) == 0:
            # Checks if the file if empty
            return "No rooms found - file is empty"

        with open(filename, 'r') as file:
            # Reads the file
            rooms = file.read().strip()

        return rooms

    def view_occupied_rooms(self, reservations_filename):
        """
        The view_occupied_rooms function loads reservations from a CSV file and uses
        check_availability from garris.py to determine which rooms are currently
        occupied or vacant based on today's date.

        The reservations file is expected to have lines in the format:
            room_number,checkin,checkout
        Example:
            1,01/15/2026,04/20/2026
        """
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)

        # Load reservations from file into a list of dicts
        reservations = []
        if os.path.exists(reservations_filename) and os.path.getsize(reservations_filename) > 0:
            with open(reservations_filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(',')
                    if len(parts) != 3:
                        continue
                    try:
                        reservations.append({
                            'room_number': int(parts[0]),
                            'checkin': validate_date(parts[1]),
                            'checkout': validate_date(parts[2])
                        })
                    except ValueError:
                        continue

        # Check each room against today's date using check_availability
        print('\n' + "Room Occupancy Status for " + str(today) + ":" + '\n')
        for room_num in range(1, 9):
            available = check_availability(room_num, today, tomorrow, reservations)
            status = "Vacant" if available else "Occupied"
            print(f"  Room {room_num}: {status}")

    def update_room_status(self):
        """
        The update_room_status function prompts the housekeeper to select a room
        and set its cleanliness status to either 'clean' or 'dirty'. The change
        is saved back to room_status.txt.
        """
        print('\n' + "Enter the room number to update (1-8), or 'skip' to exit: ")
        choice = input("Room number: ").strip()

        if choice == 'skip':
            return "No changes made."

        if not choice.isdigit() or int(choice) not in range(1, 9):
            return "Invalid room number. Please enter a number between 1 and 8."

        room_num = int(choice)

        new_status = input("Enter new status ('clean' or 'dirty'): ").strip().lower()
        if new_status not in ('clean', 'dirty'):
            return "Invalid status. Please enter 'clean' or 'dirty'."

        # Read all lines, update the matching room, write back
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(f"Room {room_num}:"):
                lines[i] = f"Room {room_num}: {new_status}\n"
                break

        with open(self.filename, 'w') as file:
            file.writelines(lines)

        return f"Room {room_num} status updated to '{new_status}'."

    def class_option(self):
        '''
        Asks user option to read reservations, book reservations, quit, or exit user.
        '''
        while True:
            option = input("View room [S]tatus, view [O]ccupied rooms, [Q]uit program, [E]xit user: ")
            if option == "S" or option == "S":
                return "status"
            elif option == 'O' or option == 'o':
                return "occupied"
            elif option == 'Q' or option == 'q':
                return "quit"
            elif option == 'E' or option == 'e':
                return "exit"
            else:
                print("Invalid optoin, enter 'B' to book, 'S' to show reservations, 'Q' to quit, or 'E' to exit")        






def main():
    """
    Runs the program.
    """
    welcome = Welcome_Screen()
    continue_flag = True
    while continue_flag == True:    # Main loop containing user select optoins, and user loops
        next_class = welcome.welcome_screen() # Select Clerk, Managment, or Housekeeping
        class_option = "continue"

        print(next_class)

        if next_class == "quit":
            continue_flag == False

        if isinstance(next_class, Clerk_Services):
            next_class.welcome()

            while class_option != "exit" and class_option != "quit": # Service Clerk loop
                
                class_option = next_class.class_option()
                
                if class_option == "exit":
                    continue_flag == True
                elif class_option == "quit":
                    continue_flag == False
                elif class_option == "book":
                    print(next_class.add_reservation())
                elif class_option == "show":
                    print(next_class.read_reservations())
                elif class_option == "menu":
                    next_class.welcome()
            class_option = "continue" # Prevents while loop being skipped if Clerk is selected a 2nd time


        elif isinstance(next_class, Hotel_Management):
            print(next_class.welcome())

            while class_option != "exit" and class_option != "quit":
                class_option = next_class.class_option()

                if class_option == "exit":
                    continue_flag == True
                elif class_option == "quit":
                    continue_flag == False
                elif class_option == "book":
                    print(next_class.add_reservation())
                elif class_option == "show":
                    print(next_class.read_reservations())
            
            class_option = "continue" # Prevents while loop being skipped if Hotel Managment is selected a 2nd time


        elif isinstance(next_class, Housekeeping):
            while class_option != "exit" and class_option != "quit":
                # print(next_class.welcome())
                # print(next_class.update_room_status())
                class_option = next_class.class_option()
                
                if class_option == "exit":
                    continue_flag == True
                elif class_option == "quit":
                    continue_flag == False
                elif class_option == "status":
                    print(next_class.room_status(ROOM_STATUS_FILE))
                elif class_option == "occupied":
                    next_class.view_occupied_rooms(RESERVATIONS_FILE)
            class_option = "continue" # Prevents while loop being skipped if Housekeeping is selected a 2nd time

        
    
    print("Program closed")
    
if __name__ == "__main__":
    main()

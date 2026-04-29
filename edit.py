"""
Contains functions for editing, reading, and validating reservations.
"""
import re
from data import load_reservations, save_reservations
from garris import validate_date


def edit_reservation(self):
	"""
	Gives a list of current reservations and prompts the user if they want to edit one.
	Allows changing individual keys of reservations.
	"""

	reservations = load_reservations() # Load the reservation json

	while 1:
		read_reservations(self) # Read and print the current reservations
		user_in = input("\nRoom number for edit or [S]kip: ").strip()

		if user_in.lower() == 's': # Exit
			return "No changes made."

		for res in reservations:
			r_num = str(res['roomNumber'])
			if user_in == r_num: # Check if the user input is a current reservation
				read_reservation(res)
				try:
					user_in = input("\nChange [R]oom #, [C]onfirmation number, [A]rrival date, [D]eparture date, "
									"[L]ast name, [F]irst name, or [E]xit: ")
					if user_in.lower() == 'q':
						print ("No changes made.")
					# Room input
					elif user_in.lower() == 'r':
						user_in = input("New room number: ").strip()
						try:
							val = int(user_in) # Is the input an integer
							if val < 1 or val > 9: # Is the input a valid room number
								raise ValueError
							res.update({"roomNumber": val})
							save_reservations(reservations)
						except ValueError:
							print("Room number must be an integer between 1 and 8.")
					# Confirmation number input
					elif user_in.lower() == 'c':
						user_in = input("New confirmation number: ").strip()
						try:
							val = int(user_in) # Is the input an integer
							if val < 1: # Input should be non-negative
								raise ValueError
							res.update({"confirmationNumber": val})
							save_reservations(reservations)
						except ValueError:
							print("Confirmation number must be a positive integer.")
					# Arrival date input
					elif user_in.lower() == 'a':
						user_in = input("New arrival date: ").strip()
						res.update({"arrivalDate": validate_date(user_in)}) # validate_date checks for good input
						save_reservations(reservations)
					# Departure date input
					elif user_in.lower() == 'd':
						user_in = input("New departure date: ").strip()
						res.update({"leaveDate": validate_date(user_in)}) # validate_date checks for good input
						save_reservations(reservations)
					# Last name input
					elif user_in.lower() == 'l':
						user_in = input("New last name: ").strip()
						res.update({"lastName": validate_name(user_in)}) # validate_name checks for good input
						save_reservations(reservations)
					# First name input
					elif user_in.lower() == 'f':
						user_in = input("New first name: ").strip()
						res.update({"firstName": validate_name(user_in)}) # validate_name checks for good input
						save_reservations(reservations)
					# Exit
					elif user_in.lower() == 'e':
						return ""
				except ValueError as err:
					print(err)


def read_reservations(self):
	"""
    The read_reservations function takes in a json file, determines if it exists and
    prints the reservations currently housed inside the file if there are any.
    """
	res = load_reservations(self.filename)
	if not res:
		return "No reservations found"

	print("\n| Room # | Conf. Num. | Arrival Date | Departure Date | Guest Name            |")
	for r in res:
		read_reservation(r)
	return ""

def read_reservation(reservation):
	"""
	Reads and displays a single given reservation.
	"""
	reservation_num = str(reservation['roomNumber'])
	confirmation_num = str(reservation['confirmationNumber'])
	arrival_date = reservation['arrivalDate']
	leave_date = reservation['leaveDate']
	name = reservation['lastName'] + ", " + reservation['firstName']
	print("|", reservation_num, " " * (5 - len(reservation_num)),
	      "|", confirmation_num, " " * (9 - len(confirmation_num)),
	      "|", arrival_date, " " * (11 - len(arrival_date)),
	      "|", leave_date, " " * (13 - len(leave_date)),
	      "|", name, " " * (20 - len(name)), "|")

def validate_name(name):
	"""
	Validates the given name begins with a capital letter, contains up to one - and/or ' ,
	otherwise contains only letters, and ends with a letter.
	"""
	try:
		if not re.fullmatch(r"[A-Z][A-Za-z]*'?[A-Za-z]*-?[A-Za-z]+", name):
			raise ValueError("Please enter a valid name. (Capital first letter, up to one - or '.)")
		return name
	except ValueError:
		raise
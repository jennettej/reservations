"""
Contains functions for adding, editing, reading, and validating reservations.
"""
import re
from data import load_reservations, save_reservations
from garris import validate_date
from miller import date_to_mmddyyyy

def add_reservation(self):
	"""
	Adds a new reservation to the reservations list.
	@param self: path of reservations json
	@return: status message
	"""
	while 1:
		try:
			reservations = load_reservations(self.filename)
			reservation_info = prompt_create_reservation(reservations)
			if reservation_info == "":
				return "Booking cancelled."
			reservations.append(reservation_info)
			save_reservations(reservations, self.filename)
			return "Added reservation successfully."
		except ValueError as err:
			return str(err) + "\nReservation not added."

def prompt_create_reservation(reservations):
	"""
	Prompts the user for information to create a new reservation.
	@param reservations: list of reservations
	@return: new reservation in json format
	"""
	print("Begin booking... [E]xit at any time.")
	user_in = input("Last name: ").strip()
	if user_in.lower() == "e":
		return ""
	last_name = validate_name(user_in)
	user_in = input("First name: ").strip()
	if user_in.lower() == "e":
		return ""
	first_name = validate_name(user_in)
	user_in = input("Confirmation number: ").strip()
	if user_in.lower() == "e":
		return ""
	confirmation_number = validate_confirm_num(user_in, reservations)
	user_in = input("Room number: ").strip()
	if user_in.lower() == "e":
		return ""
	room_number = validate_room(user_in, reservations)
	user_in = input("Arrival date: ").strip()
	if user_in.lower() == "e":
		return ""
	arrival_date = date_to_mmddyyyy(validate_date(user_in))
	user_in = input("Departure date: ").strip()
	if user_in.lower() == "e":
		return ""
	leave_date = date_to_mmddyyyy(validate_date(user_in))

	reservation_info = {
		"lastName": last_name,
		"firstName": first_name,
		"confirmationNumber": confirmation_number,
		"roomNumber": room_number,
		"arrivalDate": arrival_date,
		"leaveDate": leave_date
	}
	return reservation_info

def edit_reservation(self):
	"""
	Gives a list of current reservations and prompts the user if they want to edit one.
	Allows changing individual keys of reservations.
	@param self: path of reservations json
	@return: status message
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
						# validate_room checks for good input
						res.update({"roomNumber": validate_room(input("New room number: ").strip(), reservations)})
					# Confirmation number input
					elif user_in.lower() == 'c':
						# validate_confirm_num checks for good input
						res.update({"confirmationNumber": validate_confirm_num(input("New confirmation number: ").strip(), reservations)})
					# Arrival date input
					elif user_in.lower() == 'a':
						# validate_date checks for good input
						res.update({"arrivalDate": date_to_mmddyyyy(validate_date(input("New arrival date: ").strip()))})
					# Departure date input
					elif user_in.lower() == 'd':
						# validate_date checks for good input
						res.update({"leaveDate": date_to_mmddyyyy(validate_date(input("New departure date: ").strip()))})
					# Last name input
					elif user_in.lower() == 'l':
						# validate_name checks for good input
						res.update({"lastName": validate_name(input("New last name: ").strip())})
					# First name input
					elif user_in.lower() == 'f':
						# validate_name checks for good input
						res.update({"firstName": validate_name(input("New first name: ").strip())})
					# Exit
					elif user_in.lower() == 'e':
						return ""

					save_reservations(reservations)
				except ValueError as err:
					print(err)

def read_reservations(self):
	"""
    The read_reservations function takes in a json file, determines if it exists and
    prints the reservations currently housed inside the file if there are any.
    @param self: path of reservations json
	@return: status message
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
	@param reservation: single reservation to display
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
	@param name: name to validate
	@return: name if valid
	"""
	try:
		if not re.fullmatch(r"[A-Z][A-Za-z]*'?[A-Za-z]*-?[A-Za-z]+", name):
			raise ValueError("Please enter a valid name. (Capital first letter, up to one - or '.)")
		return name
	except ValueError as err:
		raise err

def validate_confirm_num(confirm_num, reservations):
	"""
	Validates confirmation number is a positive integer and is not already in use.
	@param confirm_num: confirmation number
	@param reservations: list of reservations
	@return: confirmation number if valid
	"""
	try:
		try:
			val = int(confirm_num)  # Is the input an integer
			if val < 1:  # Input should be non-negative
				raise ValueError
		except ValueError:
			raise ValueError("Confirmation number must be a positive integer.")
		for res in reservations:
			if val == res["confirmationNumber"]:
				raise ValueError("Confirmation number is already in use.")
		return val
	except ValueError as err:
		raise err

def validate_room(room_num, reservations):
	"""
	Validates that the room number is between 1 and 8 and that it is not already booked.
	@param room_num: room number
	@param reservations: list of reservations
	@return room number if valid
	"""
	try:
		try:
			val = int(room_num)  # Is the input an integer
			if val < 1 or val > 8:  # Is the input a valid room number
				raise ValueError
		except ValueError:
			raise ValueError("Room number must be an integer between 1 and 8.")
		# Check if room is already booked
		for res in reservations:
			if val == res["roomNumber"]:
				raise ValueError("Room already booked.")
		return val
	except ValueError as err:
		raise err

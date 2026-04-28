import json

from data import load_reservations, save_reservations
from garris import validate_date


def edit_res(self):
	"""
	Gives a list of current reservations and prompts the user if they want to edit one.
	Allows changing aspects of reservations.
	"""

	reservations = load_reservations()

	while 1:

		read_reservations(self)
		user_in = input("\nRoom number for edit or [S]kip: ").strip()

		if user_in.lower() == 's':
			return "No changes made."

		for res in reservations:
			r_num = str(res['roomNumber'])
			if user_in == r_num:
				read_reservation(res)

				user_in = input("\nChange [R]oom #, [C]onfirmation number, [A]rrival date, [D]eparture date, [L]ast name, [F]irst name, or [Q]uit: ")
				if user_in.lower() == 'q':
					print ("No changes made.")
				if user_in.lower() == 'r':
					user_in = input("New room number: ").strip()
					try:
						val = int(user_in)
						if val < 1 or val > 10:
							raise ValueError
						res.update({"roomNumber": val})
						save_reservations(reservations)
					except ValueError:
						print("Room number must be an integer between 1 and 9.")
				if user_in.lower() == 'c':
					user_in = input("New confirmation number: ").strip()
					try:
						val = int(user_in)
						if val < 1:
							raise ValueError
						res.update({"confirmationNumber": val})
						save_reservations(reservations)
					except ValueError:
						print("Confirmation number must be a positive integer.")
				if user_in.lower() == 'a':
					user_in = input("New arrival date: ").strip()
					try:
						val = validate_date(user_in)
						res.update({"arrivalDate": val})
						save_reservations(reservations)
					except ValueError:
						print("")
				if user_in.lower() == 'd':
					user_in = input("New departure date: ").strip()
					try:
						val = validate_date(user_in)
						res.update({"leaveDate": val})
						save_reservations(reservations)
					except ValueError:
						print("")
				if user_in.lower() == 'l':
					user_in = input("New last name: ").strip()
					try:
						val = user_in
						res.update({"lastName": val})
						save_reservations(reservations)
					except ValueError:
						print("")
				if user_in.lower() == 'f':
					user_in = input("New first name: ").strip()
					try:
						val = user_in
						res.update({"firstName": val})
						save_reservations(reservations)
					except ValueError:
						print("")
				if user_in.lower() == 'q':
					return ""


def read_reservations(self):
	"""
    The read_reservations function takes in a file, determines if it exists and
    returns the reservations currently housed inside the file if there are any.
    """
	res = load_reservations(self.filename)
	if not res:
		return "No reservations found"

	print("\n| Room # | Conf. Num. | Arrival Date | Departure Date | Guest Name            |")
	for r in res:
		read_reservation(r)
	return ""

def read_reservation(reservation):
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
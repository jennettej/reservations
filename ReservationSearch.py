# ReservationSearch.py
# Author: Wesley Murray II
# Search thru reservation entries.
# Could possibly make a sorting function if we
# want to make searching by a specific dictionary property
# more efficient

from data import load_reservations, save_reservations
from edit import read_reservation as read_res

class ReservationSearch:
    def searchByProperty(arr,propertyName,check):
        # arr represents a list of dictionaries.

        # For each item in array,
        # see if the property we're searching for exists
        # and then compare it to the check variable.
        for i in arr:
            if (propertyName in i) and (i[propertyName]==check):
                return i
        
        return None
    
    def caseInsensitiveSearch(arr,propertyName,check):
        # arr represents a list of dictionaries.

        # For each item in array,
        # see if the property we're searching for exists
        # and then compare it to the check variable.
        # Use the lowercase version of each property.
        for i in arr:
            if (propertyName in i) and (i[propertyName].lower()==check.lower()):
                return i
        
        return None


def search_reservation(res):
    """
    Adds a new reservation to the reservations list.
    @param res: path of reservations json
    @return: status message
    """
    while 1:
        try:
            reservations = load_reservations(res.filename)
            search_query = input("Input last name: ").strip()

            search_result = ReservationSearch.caseInsensitiveSearch(reservations,"lastName",search_query)

            if search_result is not None:
                print("Found reservation!")
                print("| Room # | Conf. Num. | Arrival Date | Departure Date | Guest Name            |")
                read_res(search_result)
                return ""
            else:
                return "Could not find reservation."
        except ValueError as err:
            return str(err) + "\nWas unable to find a reservation."


if __name__=="__main__":
    print("Testing ReservationSearch.py; search functions.")
    # Test array using fake data. Might not be final layout of data.
    testArr = [
        {
            "lastName": "Michael",
            "firstName": "Jichael",
            "confirmationNumber": 12345678,
            "roomNumber": 101,
            "arrivalDate": "04-06-2026",
            "leaveDate": "04-10-2026"
        },
        {
            "lastName": "Adam",
            "firstName": "Jadam",
            "confirmationNumber": 34567890,
            "roomNumber": 201,
            "arrivalDate": "04-09-2026",
            "leaveDate": "04-14-2026"
        },
    ]

    print("Find last name 'Adam'...")
    print(ReservationSearch.searchByProperty(testArr,"lastName","Adam"))
    print("Find last name 'Nobody'...")
    print(ReservationSearch.searchByProperty(testArr,"lastName","Nobody"))
    print("Use property 'apples', which doesn't exist...")
    print(ReservationSearch.searchByProperty(testArr,"apples","nothing"))
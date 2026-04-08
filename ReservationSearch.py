# ReservationSearch.py
# Author: Wesley Murray II
# Search thru reservation entries.
# Could possibly make a sorting function if we
# want to make searching by a specific dictionary property
# more efficient

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
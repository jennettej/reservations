# Search functions.
# Search thru reservation entries.
# Most searches are brute because sorting & keeping sorts
# might be too much weight
# However, we could probably keep it sorted under
# one attribute, specifically whatever property is "most important"

class ReservationSearch:
    def searchByProperty(arr,propertyName,check):
        for i in arr:
            if (propertyName in i) and (i[propertyName]==check):
                return i
        
        return None


if __name__=="__main__":
    print("Testing murray.py; search functions.")
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
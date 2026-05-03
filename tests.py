# Jonathan Miller
# This program tests the reservation system by 
# creating, reading, searching, and closing reseravations.

import json
from data import load_reservations, save_reservations
from ReservationSearch import ReservationSearch
from miller import close_reservation

TEST_FILE = 'reservations.json'

print("=== Running Tests ===")

# Backup original
try:
    with open(TEST_FILE, 'r') as f:
        backup = json.load(f)
except:
    backup = []


print("\n1. Test Create Reservation:")
res = load_reservations(TEST_FILE)
new_res = {
    "lastName": "Test",
    "firstName": "User",
    "confirmationNumber": 999999,
    "roomNumber": 5,
    "arrivalDate": "04-23-2026",
    "leaveDate": "04-25-2026"
}
res.append(new_res)
save_reservations(res, TEST_FILE)
saved = load_reservations(TEST_FILE)
print(f"  Created: {new_res}")
print(f"  Saved count: {len(saved)}")


print("\n2. Test Read Reservations:")
loaded = load_reservations(TEST_FILE)
print(f"  Loaded reservations: {len(loaded)}")
if loaded:
    print(f"  Latest reservation: {loaded[-1]}")


print("\n2b. List All Reservations:")
for i, res in enumerate(loaded):
    print(f"  {i+1}: {res}")


print("\n3. Test Search by lastName 'Test':")
search_res = ReservationSearch.searchByProperty(loaded, "lastName", "Test")
print(f"  Search result: {search_res}")


print("\n3b. Test Search by confirmationNumber 999999:")
search_conf = ReservationSearch.searchByProperty(loaded, "confirmationNumber", 999999)
print(f"  Search result: {search_conf}")


print("\n4. Test Close Reservation (confirmation # 999999):")
close_reservation(loaded, 999999)
save_reservations(loaded, TEST_FILE)
after_close = load_reservations(TEST_FILE)
print(f"  After close count: {len(after_close)}")
search_after = ReservationSearch.searchByProperty(after_close, "lastName", "Test")
print(f"  Search after close: {search_after}")


# Restore
save_reservations(backup, TEST_FILE)
print("\nTests complete. Original data restored.")
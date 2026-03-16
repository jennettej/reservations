import json
import os

def getInput():
	try:
	  os.remove("reservations.json") #https://www.w3schools.com/python/python_file_remove.asp
	  print("File exists, deleting...")
	except:
	  print("No file exists, creating...")
	f = open("reservations.json","x")
	v1 = input("Name here: ")
	v2 = input("Arrival date here: ")
	v3 = input("Stay length here: ")
	v4 = input("Guest number here: ")
	x = {
	  "name": v1,
	  "date": v2,
	  "length": v3,
	  "guests": v4
	}
	y = json.dumps(x)
	print(y)
	f.write(y)
	f.close()

getInput()
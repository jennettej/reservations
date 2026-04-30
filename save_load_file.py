import json #import everything
import os #https://www.w3schools.com/python/python_file_remove.asp

def getInput():
	'''getInput: gets a bunch of inputs from the user and writes them to a file'''
	try: #if a file already exists
	  f = open("reservations.json","a") #open it
	except: #if not, do nothing
	  print("No file exists, creating...")
	  f = open("reservations.json","x") #make a new file
	v1 = input("Name here: ") #get a list of inputs
	v2 = input("Arrival date here: ")
	v3 = input("Stay length here: ")
	v4 = input("Guest number here: ")
	x = {#arrange them into a dictionary
	  "name": v1,
	  "date": v2,
	  "length": v3,
	  "guests": v4
	}
	y = json.dumps(x) #convert the dictionary to json format
	print(y)
	f.write(y) #write the json to the file
<<<<<<< Updated upstream
	f.close() #close the file

getInput()
=======
	f.close() #close the file
>>>>>>> Stashed changes

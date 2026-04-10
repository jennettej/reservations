def list_write(file1,file2):
  '''list_write: takes the contents of 1 file and writes them to another'''
  try: #if file exists
   f1 = open(file1, "r") #open it
   res = "test" #dummy string
   res = str(f1.readlines())+"\n" #reads the contents of the file
   print("Things to add: "+res) #prints it out, any test prints like this can be removed later
   f2 = open(file2, "a") #opens file to write to
   f2.write(res) #writes it
   f1.close() #closes files after finished writing
   f2.close()
   print("Reservation successfully written") #print to show that it worked
   f3 = open(file2,"r") #reads from the file
   print(str(f3.readlines())) #test print, to make sure it worked
   f3.close() #closes this file too
  except: #if it doesn't exist
    print("Error: no existing file to write to") #print letting you know it doesn't exist

list_write("reservations.json","list.txt") #FILES DON'T GET CREATED AUTOMATICALLY, I ALREADY FIGURED OUT HOW TO DO THAT IN SAVE_LOAD_FILE
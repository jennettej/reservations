#try:
f1 = open("reservations.json", "r")
res = "test"
res = str(f1.readlines())
print("Things to add: "+res)
f2 = open("list.txt", "a")
f2.write(res)
f1.close()
f2.close()
print("Reservation successfully written")
f3 = open("list.txt","r")
print(str(f3.readlines()))
f3.close()
#except:
#       print("Error: no existing file to write to")





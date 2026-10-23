full_name = input("Enter full name")
Staff_number = input("enter Staff Number")
level = input("enter level")

if full_name =="":
    print ("Name cannot be left empty")
else:
    print("Accepted")
    

if Staff_number.isdigit():
    print ("Numeric staff number accepted")
else:
    print("staff number can only be numeric")


if level.isdigit():
    print ("Numeric level accepted")
else:
    print("level can only be numeric")
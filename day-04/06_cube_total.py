import math
n = int(input ("enter number:"))
if n!=0:
    print("")
    total = 0
    for x in range (1,n+1):
        cube = x**3
        print(cube,end ="")
        
        total = total + cube
    print("")
    print("")
    
    print(f"The total number is {total:.0f}")
else:
    print("number cannot be 0")
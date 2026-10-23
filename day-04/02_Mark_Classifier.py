mark = int(input("Please enter a mark"))

if mark >0 and mark <= 100:   
    if mark >=80 and mark <=100 :
    
        print("Outstanding")
        
    elif mark >=70 and mark <=79:
         print("Highly Competent")
         
    elif mark >=50 and mark <=69:
         print("competent")
        
    elif mark >=40 and mark <=49:
         print("Not Yet Competent")
         
    elif mark >=0 and mark <=39:
         print("Not achieved")
         
         
         
else:
    print("not valid")
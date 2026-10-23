marks = []
i = 0

mark = int(input("Please enter Mark(or -1 to stop"))
 

while mark !=-1:
    marks.append(mark)
    
  #  marks[i] = mark
 #  i +=1
    
mark = int(input("Please enter Mark(or -1 to stop"))

print(f"Our list has {len(marks)} elements")
    
for x in range(len(marks)):
    print(marks[x])
    
sum =0
for x in range(len(marks)):
    mark = marks[x]
    sum = sum + mark
    
print(f"The sum of all marks = {sum}")

#Get Total

total = 0
for x in range (len(marks)):
    mark = marks[x]
    total=total + mark
    
avg = total/len(marks)
print(f"The average of all marks ={avg}")
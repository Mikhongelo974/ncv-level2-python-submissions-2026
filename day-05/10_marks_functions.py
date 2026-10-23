get getMarks():
    marks = []
    mark = int(input("enter marks(or -1 to stop)"))
    
    while mark !=-1:
        mark.append(mark)
        mark = int(input("enter marks(or -1 to stop)"))
        
        return marks
print(f"Our list has {len(marks)} elements")

def print_list_size(marks):
    print(f"our list has {len(marks)} elements")
    
def print_marks(marks):
    for x in range(len(marks)):
        print(f"Mark {x+1} is {marks[x]}")
        
def get_sum_of_marks(marks):
    sum = 0
    for x in range(len(marks)):
        mark = marks[x]
        sum = sum + mark
        return sum
print(f"The sum of all marks = {sum}")

def determine_highest(marks):
    highest = 0
    for i in range(len(marks)):
        current_mark=marks[i]
        if (current_mark>highest):
            highest=current_mark
    print("The highest mark is {highest}")
    
    menu="Press 1: Capturing marks\n"
    menu+="press 2:Check number of marks\n"
    menu+="press 3: To calculate average of marks\n"
    menu +="Press 4: To find highest mark\n"
    menu +="Press -1: To exit"
    
    print(menu)
    choice = int(input(":Make your choice"))
    
    entered_marks=[]
    if choice ==1:
        entered_marks = get_marks()
        print(entered_marks)
    elif choice ==2:
        print_list_size(entered_marks)
    elif choice ==3:
        calc_sum=get_sum_of_marks(entered_marks)
        print("Sum of all marks=",calc_sum)
    elif choice ==4:
        determine_highest(entered_marks)
        
        
    else print("not on the menu")
    
    
    print(menu)
    choice = int(input(":Make your choice(-1 to exit)"))
        
    
    
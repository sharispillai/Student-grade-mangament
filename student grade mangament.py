def calculate_average(marks):
    total=sum(marks)
    average=total/len(marks)
    return average
def get_grade(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    elif average>=70:
        return "c"
    elif average>=60:
        return "D"
    else:
        return "F"
marks=[]
for i in range(5):
    mark=int(input(f"enter the mark for subjects{i+1}:"))
    if mark >= 0 and mark<=100 :
     marks.append(mark)
    else:
     print("invalid marks,please enter the marks between 0 to 100")
average=calculate_average(marks)
grade=get_grade(average)
print("The marks",marks)  
print("The average marks:",average)  
print("The grade is:",grade)

    
"""
    Write a python program to take student info name, age, branch,sub1, sub2, sub3 and calculate grade, percentage, and display records.
"""

student_name = input("Student name: ")
student_age = int(input("Student age: "))
student_branch = input("Student branch: ")
sub1 = int(input("Subject 1 marks: "))
sub2 = int(input("Subject 2 marks: "))
sub3 = int(input("Subject 3 marks: "))
percentage = (sub1 + sub2 + sub3) / 300.0 * 100

def grade_cal(percentage):
    if 90 <= percentage <= 100:
        return "Grade A"
    elif 80 <= percentage < 90:
        return "Grade B"
    elif 70 <= percentage < 80:
        return "Grade C"
    elif 60 <= percentage < 70:
        return "Grade D"
    elif 50 <= percentage < 60:
        return "Grade E"
    else:
        return "Fail"

print("-----Student Record-----")
print(f"Name : {student_name}")
print(f"Age : {student_age}")
print(f"Branch : {student_branch}") 
print(f"Percentage: {percentage:.2f}")
print(f"Grade: {grade_cal(percentage)}")
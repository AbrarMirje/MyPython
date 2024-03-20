rno = int(input("Enter Roll No: "))
name = input("Enter Student Name: ")
m1 = int(input("Enter Marks1: "))
m2 = int(input("Enter Marks2: "))
m3 = int(input("Enter Marks3: "))
m4 = int(input("Enter Marks4: "))
m5 = int(input("Enter Marks5: "))

Total = m1 + m2 + m3 + m4 + m5
Percentage = Total / 5

if Percentage >= 70:
    result = "Distinction"
elif Percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("            DYP-ATU               ")
print("         MCA SANDWICH             ")
print("\nResult:")
print(f"Roll Number: {rno}")
print(f"Name: {name}")
print(f"Total Marks: {Total}")
print(f"Percentage: {Percentage:.2f}")
print(f"Grade: {result}")

marks = [m1, m2, m3, m4, m5]
subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
for i in range(len(marks)):
    if marks[i] < 40:
        print(f"Your marks in {subjects[i]} are less than 40. You have failed in {subjects[i]}.")
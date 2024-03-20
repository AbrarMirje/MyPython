"""
    Write a program to take a person details as name, age, slary, company, designation and add new elements in dictionary.
"""

name = input("What's name? ")
age = int(input("What's age? "))
salary = float(input("What's salary? "))
companyName = input("What's company name? ")
designation = input("What's designation? ")
employee_dict = {
    "name": name,
    "age": age,
    "salary": salary,
    "company": companyName,
    "designation": designation,   
}
print("--------------------------")
for key, value in employee_dict.items():
    print(key + ":", value)
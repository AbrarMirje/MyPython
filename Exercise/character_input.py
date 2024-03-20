import datetime
user_name = input("Enter user name: ")
age = int(input("Enter age: "))

current_year = datetime.datetime.now().year
century = current_year - age + 100
print(f"{user_name} will do century in {century}")
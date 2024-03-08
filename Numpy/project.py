import numpy as np

def user_info():
    user_input = int(input("Enter grade: "))
    grade_arr = np.array([])
    grade_arr = np.append(grade_arr, user_input)
    return grade_arr

print(f"Grade: {user_info()}")
import numpy as np

# numbers = np.array([10,20,30,40,'Abrar', 60.36, True])
# print(type(numbers)) # <class 'numpy.ndarray'>  nd --> N-Dimensional
# print(numbers)
# print(numbers.shape) # shape is used to check number of rows and columns in an array


# Multi-dimensional Arrays

first = [10,20,30,5]
second = [1,2,3,5]
third = [22,33,44,5]

py_arr = np.array([first, second, third])
# print(py_arr.size) # Tells that how many number of elements are present inside an array
print(py_arr.shape)
print(py_arr)
print(py_arr.reshape(4, 3))
print(py_arr.shape)










# Creating an three list
# Doubt 1) Why this is not possible ?
# list1 = [10,20,30,40,50]
# list2 = [9,6,3,8,5]
# list3 = [1,2,3,4,5,6,7,8,9]

# arr = np.array([list1, list2, list3])
# print(arr)
# print(arr.shape)


# Doubt 2) Why this True interanlly treated as a 1, and what if i want to use bool data like True of False ?
# l1 = [10,20,30,40]
# l2 = [True, 1,2,3]

# arr2 = np.array([l1, l2])
# print(arr2)
# print(type(arr2))





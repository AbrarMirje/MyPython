import numpy as np

arr1 = np.arange(0, 10, 2)
# print(arr1)

arr2 = np.linspace(1, 10, 50)
# print(arr2)

# copy() function and broadcasting 
arr3 = np.array([1,2,3,4,5,6,7,8,9,10])
arr3[3:] = 500
# print(arr3)

# Some conditions are very useful in Exploratory data analysis
val = 10
arr4 = np.array([20,30,5,60,90,1])
# We can do lot of operations 
# print(arr4 < val)
# print(arr4 * val)
# print(arr4 % val)

# If i want exact elements which are less than 10
# print(arr4[arr4 < val])


# Some more plays
# 1) Creating an array with only one, default it is float
arr5 = np.ones(4, dtype=int)
print(arr5)

# 2) Creating multi-dimensional array with one
arr6 = np.ones((2, 3), dtype=int)
print(arr6)
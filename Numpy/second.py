import numpy as np

arr = np.array([
    [1,2,3,4,5],
    [10,20,30,40,50],
    [111,222,333,444,555],
])

# print(arr)
# print(arr[0, 3]) # Accessing elements using index
# print(arr[:,:2]) # Accessing elements using slice operator


another_arr = np.random.randint(0, 10, (3,4))
# print(another_arr)
# print(type(another_arr))

# Choose the random number from arr
arr2 = np.array([3.2,52.2,90.36,47.20])
new_arr = np.random.choice(arr2);
print(new_arr)
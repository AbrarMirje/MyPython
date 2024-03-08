import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(np.sum(arr))
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.abs(arr))
# print(arr.reshape(2, 6))

# How to replace element in an array
# 1) First convert multi-dimensional array into single dimensional array
arr_flatten = arr.flatten()
print(arr_flatten)

# 2) Then use put() to insert element at specific position
arr_flatten.put(3, 65)
print(arr_flatten)

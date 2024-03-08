import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Append an element to the end of the array
arr = np.append(arr, 6)

# Extend the array with another array
arr = np.concatenate((arr, np.array([7, 8, 9])))

# Insert an element at a specific index
arr = np.insert(arr, 0, 0)  # Inserting 0 at index 0

# Remove an element at a specific index
arr = np.delete(arr, 0)  # Removing element at index 0

# Pop an element from the end of the array
popped_element = arr[-1]
arr = np.delete(arr, -1)  # Remove last element

# Find the index of a specific value
index = np.where(arr == 3)[0][0]

# Count occurrences of a specific value
count = np.count_nonzero(arr == 2)

print("Updated Array:", arr)
print("Popped Element:", popped_element)
print("Index of 3:", index)
print("Count of 2:", count)

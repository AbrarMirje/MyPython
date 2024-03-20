# List supports operations like concatenatiion
square = [1,4,9,16,25]

data = square + [10,20,30,40,50]
# print(data)

# List is mutuble (can be change)
cubes = [1,8,27,65,125]
# the cube of 4 is 64, not 65!
# print(4**3) 
cubes[3] = 64
# print(cubes)

# append() in list
cubes.append(99)
# print(cubes)

# list reference the same object
rgb = ['Red', 'Green', 'Blue']
rgba = rgb
id(rgba) == id(rgb)   # they reference the same object
# so changing one will affect another
rgba.append("Alph")
# print(rgb)

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
# print(correct_rgba)

# We can perform remove and replace operations using slice operator

letters = ['a', 'b','c', 'd', 'e']
print(letters)
letters[1:4] = ['B', 'C', 'D'] 
# print(letters)

# now remove them
letters[1:4] = []
# print(letters)

# now remove all the data from list
letters[:] = []
# print(letters)

# built in function len() in list is alos possible
numbers = [10,20,30,40,50,60]
# print(len(numbers))

# Nesting the list
a = [10,20,30]
b = ['A', 'Z']
x = [a,b]
# print(x)
# print(x[0])
# print(x[0][1])






# Operatoins on list
fruits = ['apple', 'banana', 'grapes', 'watermelon']
fruits.insert(1, 'kiwi') # insert() will push the existing element and will take the position of that element
fruits.extend((10,20,30)) # we can also extends the other collections type
# print(type(fruits))
print(fruits)

fruits.pop() # will remove the last element of the list
fruits.pop(2)  # will remove the element at index 2 (here grapes)

print(fruits.reverse) # will reverse the homogeneous list
print(fruits.sort)  # will sort in ascending order
print(fruits.sort(reverse=True))  # will sort in descending order

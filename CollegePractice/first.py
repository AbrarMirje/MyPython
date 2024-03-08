import numpy

numbers = numpy.array([10,20,30,40])

for i in numbers:
    print(i, end=" ")  


print(range(6))

x = {'Abrar', 10, 10}
print(x)

z = 10.4648846546548614654846546844654684853565464684897961531564654154684848431654801465465489484848484844 
print(type(z))

tuples = 10, 20, 30, 'Abrar'
print(type(tuples))
print(tuples)

tuples1 = 'Abrar', 'Saalim'
print(type(tuples1))

sets = {10, 'Abrar'}
print(sets)
sets.add(10.2569)
print(sets)


# Question
string_type = 'Abrar'
print(type(string_type))
print(string_type)

############################

another_val = str(123)
print(type(another_val))


string1 = "Hello "
string2 = "Hello"
print(string1 == string2)   # White space matters


change = "Welcome "
print(change.replace('W', 'Z'))
# print(change)

print(type(change))
print(change[-1])

print(change[::-1])
print(change[3 : -2])
print(change[4:1]) # It will always represents the blank 


listData = [10, 20, 60, 50]
print(listData[3 : 1])
print(listData)

print(change.upper())
print(change.count('  '))
# print("Find: " , change.find('e'))

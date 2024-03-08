my_list = []
# Adding elements in the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])

# for element in my_list:
#     print(element)


# We can add elements directly also
new_list = [10, 20, 30.2, 'a', True, None]
# for element in new_list:
#     print(element)

##################################################################

# Exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.remove(1)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)



digit_list = []

for element in range(1, 10, 2):
    digit_list.append(element)

for element in digit_list:
    print(element)

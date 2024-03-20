my_name = 'AbrarMirje1'

print(my_name.isalnum())        # check if all char are numbers (a-z) and (0-9), not alphanumeric: (space)!#%&? etc
print(my_name.isalpha())        # check if all char in the string are alphabetic (a-z)
print(my_name.isdigit())        # test if string contains digits (0-9) and exponential
print(my_name.isdecimal())      # test if string contains decimal
print(my_name.istitle())        # test if string contains title
print(my_name.isupper())        # test if string contais upper case
print(my_name.islower())        # test if string contains lowe case
print(my_name.isspace())        # test if string contains space
print(my_name.endswith('e'))    # test if string ends with e
print(my_name.startswith('A'))  # test if string starts with A
print(my_name[0:]);

print(len(my_name))

num = "123456"
print(num.count("6")) # return number of occurence
print(num.find("6")) # return index number
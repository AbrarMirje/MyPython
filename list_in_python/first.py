lst = ['Abrar', 100, 20.59, True, 'Hello']

lst.append(['John', 'Alex', 'Steve']) # Appending list inside the list
lst.insert(0, 'Shiroli') # inserting data at specified position
lst.extend([8, 9]) # it added elements seperately
print(lst)

another_list = [10,20,30,40,50]
print(sum(another_list)) # sum() is predefined funtion used to sum the integer list elements
another_list.pop() # it removes the last elements from the list
another_list.pop(1) # it removes the first 2nd element from the list
print(another_list)


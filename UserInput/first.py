# variable = input("list seperated by space")
# list1 = variable.split()
# print(list1)

# variable = input("list seperated by the space")
# list1 = list(map(int, variable.split()))
# print(list1)

list1 = []

r = int(input("Enter range "))
for _ in range(r):
    list1.append(int(input("Enter element: ")))
    
for i in range(r):
    print(i, end=" ")
    print(list1[i])

# print(list1)

elements = set()
print(type(elements))

items = {}
print(type(items))

num={1,1,2,3}
print(num)

sum=set((1,2,3,4,5))
print(sum)
print(type(sum))

# data={"python","dsa"}
# data.add("mca")
# data.add(13)#add single elements
# data.add(("bca"))
# data.update('Abrar', 'Java')
# print(data)

data={"python","dsa"}
data.update(("dsa","mca")) #add multiple elemnts
data.update(data)
print(data)
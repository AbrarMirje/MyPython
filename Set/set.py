#set is created by using
#set() method
#curly braces{}
"""set={12,23,24}
print(set)"""

"""#create empty set
sum=set()  #create empty set
print(sum)
sum={}  #create empty dictionary
print(type(sum))"""

"""#create set of intiger
sum={1,2,3,4,5}
sum=set([1,2,3,4,5])
print(sum)

#create set of sting type
sum={"dyp","atu"}
sum1=set(['a','e','i','o','u'])
print(sum1)

#creating set of mixed data type
sum={1,'s',2.4}
print(sum)

#duplicate item in a set
num={1,1,2,3}
print(num)

#set() constructor to make a set(type casting)

sum=set((1,2,3,4,5))
print(sum)
print(type(sum))"""


"""#adding element to set

#using add() method
data={"python","dsa"}
data.add("mca")
data.add(13)#add single elements
data.add(("bca"))
print(data)

#using update() method 
data={"python","dsa"}
data.update("dsa","mca") #add multiple elemnts
data.update(data)"""


"""#Remove elements from set
#1)discard()
data={12,23,45,15}
data.discard(100) #it not generate error if element is not present only give same set as a output
data.discard(23)
print(data)
#2)remove()
data={12,23,45,15}
#data.remove(100)  #it generate error if element is not present
data.remove(23)
print(data)
#3)pop()
data={12,23,45,15}
data.pop()#it remove last element and without any arguments
print(data)"""


"""#SET OPERATIONS
#1)Union  #use | (pipe) or union
#duplicate not allowed
A={1,3,5,9}
B={0,2,4,10}
print('Union=',A|B)
print(A.union(B))

A={1,3,5,9}
B={0,2,4,10,9}
print('Union=',A|B)

#2)Intersection
#common
A={10,3,15,9}
B={20,15,9,10}
c={3,10,15}
print('Intersection=',A&B&c)
print(A.intersection(B,c))

#3)Difference
A={1,3,5,9}
B={0,1,4,10}
print('Difference=',A-B)
print(A.difference(B))

#4)Symmetric difference
A={1,3,5,9}
B={0,1,4,9}
print('Symmetric=',A^B)
print(A.symmetric_difference(B))"""


"""#que
element1=(input("enter element in set 1 "))
set1=set(map(int,element1.split()))

element2=(input("enter element in set 2 "))
set2=set(map(int,element2.split()))

print(set1)
print(set2)

print('Union=',set1|set2)
print('Intersection=',set1&set2)
print('Difference=',set1-set2)
print('Symmetric=',set1^set2)"""



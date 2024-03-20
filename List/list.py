#creating empty list
list1=[]
print(list1)

#creating list of numbers
list1=[10,15,20,90,14]
print("\nlist of numbers:")
print(list1)

#creating list of String
list1=["dyp",'ATU',"""Talsannd"""]
print("\nlist of strings:")
print(list1)
print("_____________________________________")

#creating duplicate elemts
list1=[1,2,4,4,3,3,3,6,5,2]
print(list1)
#creating allows mix duplicate strings
list1=["dyp",25,"dyp",10.28,"talsande"]
print(list1)
print("_____________________________________")

#nested list with mixed types
list1=[1,2,[4,4,"atu",3],3,6,5,2]
print(list1)
#creating a list with tuple elemnts
list1=[1,2,(4,4,"atu",3),3,6,5,2]
print(list1)
#creating list multi-demensional list
list1=[[1,2,4],[4,"atu",3],[3,6,5,2]]
print(list1)
print(list1[0][1])
print("_____________________________________")

#Taking input of a list
variable=input("enter elements: ")
list1=variable.split()
print(list1)
print(type(list1))

#convert into int
"""list2=list(map(int,variable.split())) #map method used to convert one datatype to another
print(list2)
print(type(list2))"""

"""element=input("enter elements(space-separated):")
list1=element.split()
print('list is:',list1)

#enter intiger elemnt in list
list1=[]
n=int(input("enter number: "))
for i in range(0,n):
    list1.append(int(input("enter item:")))
print(list1)"""

"""#print index with there values
list1=[]
n=int(input("enter number: "))
for i in range(0,n):
    list1.append(int(input("enter item:")))
for item in range (n):
    print(item,end=" ")
    print(list1[item])"""

"""#remove any element
list=[10,11,12,13,14]
print("original list: ")
for i in range(len(list)):
    print(i,end=" ")
    print(list[i])
list.remove(12)
print("\n list after remove elemnt: ")
for i in range(len(list)):
    print(i,end=" ")
    print(list[i])"""

"""list=[10,11,12,13,14]
print("original list: ")
for i in range list:
    print(i,end=" ")
    
list.remove(2)
print("\n list after remove elemnt: ")
for i in list:
    print(i,end=" ")
    print(list[i])"""
    



"""#Accessing elements from list
list1=[10,25,65,43,"80",30,"he",6.8]
print(list1[0])
print(list1[-1])
print(list1[2])
print(list1[-8])
print(list1[6.8])
print(list1[-9])"""

"""#indexing of list
list1=[["dyp",25],["mca",10,9],["he",6,8.9]]
print(list1[0][1])
print(list1[1][0])
print(list1[2][2])

#List split
list1=[1,2,3,4,5,6,7]
print(list1[:])
print(list1[0:])
print(list1[2:])
print(list1[:3])
print(list1[1:7])
print(list1[1:6:2])"""

"""#List split
list2=[10,20,30,40,50,60,70]
print(list2[-2])
print(list2[-3:])
print(list2[:-2])
print(list2[-3:-2])
print(list2[-6:-2])
print(list2[-3:2])
print(list2[1:-2])"""

"""#Add element in list
#1)insert method()
list1=[2,3,5,7]
list1.insert(0,11)
print("list: ",list1)

list1=[2,3,5,7]
list1.insert(3,11)
print("list: ",list1)

list1=[2,3,5,7]
tuple=(10,20)
list1.insert(2,tuple)
print("list: ",list1)

list1=[2,3,5,7]
list2=(15,25)
list1.insert(0,list2)
print("list: ",list1)"""

#2)append()
"""list1=[2,3,5,7]
list1.append(11)
print("list: ",list1)

list1=[2,3,5,7]
list1.append(13,11)
print("list: ",list1)

list1=[2,3,5,7]
tuple=(10,20)
list1.append(tuple)
print("list: ",list1)

list2=["hii","ok"]
list1.append(list2)
print("list: ",list1)"""

#3)extend()
"""list1=[1,2,3,4]
list2=[10,20]
list1.extend(list2)
print("List :",list1)"""

"""#Remove Elements from list
#1)remove() ==>remove value not a according to index
list1=[1,2,3,4]
list1.remove(3) #pass value for parameter
print("List :",list1)

list1=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(1,5):
    list1.remove(i)
print(list1)

# Appending elements in the list
list1=[]
n=int(input("enter number of elements: "))
for i in range(0,n):
    list1.append(int(input("enter the item: ")))
print(list1)
list1.remove(2)
print(list1)"""



#2)pop ==>pop elements according to there indexing
"""list2=[1,2,3,4]
list2.pop()
print("List :",list2)

list2=[1,2,3,4]
list2.pop(2) #pass index for parameter
print("List :",list2)"""

#Update Element In List
#update elements in a list
list1=[1,2,3,4,5]
list1[3]=20
print(list1)

#update multiple element in a list
list1=[1,2,3,4,5]
list1[1:3]=15,25
print(list1)

#update last elements in a list
list1=[1,2,3,4,5]
list1[-1]=30
print(list1)











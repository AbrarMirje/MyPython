str1="hello"
str2="welcome"
str3="hello"

#compare String
print(str1==str2)
print(str1==str3)
print(str2==str3)

#concate string
print(str1+str2)

#string repetition
print(str1*3)
print("_____________________________________")

#access String characters
string1="welcome"
print("initial string:")
print(string1)

print("First charater of string is : ") #POSITIVE INDEXING
print(string1[0])

print("Last charater of string is : ")    #NEGATIVE INDEXING
print(string1[-1])
print("_____________________________________")
#String Slicing
#use to access substring of given string
str="welcome"
print(str[:])
print(str[0:])
print(str[:6])
print(str[:4])
print(str[0:3])
print(str[2:5])
print("_____________________________________")
print(str[-2])
print(str[-3:-2])
print(str[-6:-2])
print(str[3:-2])
print(str[-3:2])
print("_____________________________________")
#Reverse String
str="welcome"
print(str[0:2:4])
print(str[::-1]) #reverse the string
print("_____________________________________")
#String Methods
#1)delete
del(str)
#del(str[2]) #show error..because string is immutable
#2)update
#3)Reassign

#4)Length
str="welcome"
print(len(str))
#5)upper
print(str.upper())
#6)lower
print(str.lower())
#7)count #find number of occurance
print(str.count("e"))
#8)find #find index number of perticular place of character
print(str.find("e"))
#9)replace
print(str.replace("w","h"))
print("_____________________________________")
#count and find
arr="123456"
print(arr.count('56'))
print(arr.count('560'))
print(arr.find('6'))
print(arr.find('8'))




    



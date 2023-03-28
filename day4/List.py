#Example : how to create a list
'''mylist1=[1,2,3,4,5,6]
mylist2=["apple", "banana", "cherry",]
mylist2=["apple", 1, "cherry",]
print((mylist2)[-1]) #output cherry'''

#Example: range of indexes
'''mylsit=["orange","banana","cherry","apple","kiwi","melon","mango"]
print(mylsit[2:5]) #output ['cherry', 'apple', 'kiwi']
print(mylsit[-4:-1]) #output ['apple', 'kiwi', 'melon']'''

#Example: chnage item value
'''mylist=["orange","banana","cherry","apple","kiwi","melon","mango"]
mylist[0]="water melon"
print(mylist) #output ['water melon', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango']'''

#Example:read list item using loop
'''mylist=["orange","banana","cherry","apple","kiwi","melon","mango"]
for i in mylist:
    print(i)'''
#Example:check if the item exist in the list or not
'''mylist=["orange","banana","cherry","apple","kiwi","melon","mango"]
if "apple" in mylist:
    print("Apple is present")
else:
    print("Not present")'''
#Example:list length
'''mylist=["orange","banana","cherry","apple","kiwi","melon","mango"]
len(mylist)
print(len(mylist))'''

'''#Example:add items ---> append() and insert()
mylist=["orange","banana","cherry","apple","kiwi","melon","mango"]
#mylist.append("strawberry")
mylist.insert(1, "strawberry")
#print(mylist) #output ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']
print(mylist)['orange', 'strawberry', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango']'''

#Example:remove item from the list use #pop()
'''#Approach 1
mylist = ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']
mylist.pop(7)
print(mylist)'''
'''#Approach 2
mylist = ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']
del mylist[3] #del is a key word not a function
print(mylist)'''

'''#Approach 2
mylist = ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']
mylist.clear() #clear is a function
print(mylist) #output []'''

'''#Example: copy list
mylist1= ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']
mylist2=list(mylist1)
print(mylist1)'''

'''#Example: copy list using copy()
mylist1= ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']
mylist2=mylist1.copy()
print(mylist2)'''

#Example: joining lists using looping statement
'''mylist1= ['orange', 'banana', 'cherry', 'apple']
mylist2=['kiwi', 'melon', 'mango', 'strawberry']
for i in mylist2:
    mylist1.append(i)
print(mylist1) #output ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']'''

#Exmaple using extend function
'''mylist1= ['orange', 'banana', 'cherry', 'apple']
mylist2=['kiwi', 'melon', 'mango', 'strawberry']
mylist1.extend(mylist2)
print(mylist1)#output ['orange', 'banana', 'cherry', 'apple', 'kiwi', 'melon', 'mango', 'strawberry']'''












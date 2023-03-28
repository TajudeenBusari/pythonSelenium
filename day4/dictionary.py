#Dictionary is a form of key and value base. It is unordered but indexed
'''mydict={"product1":100, "product2":200, "product3":400}

print(mydict)'''

#Example2:
'''mydict={"product1":100,
        "product2":200,
        "product3":400}

print(mydict["product1"])'''

#using get()
'''mydict.get("product2")
print(mydict.get("product2"))'''


#Example: change values in Dict
'''mydict={"product1":100,
        "product2":200,
        "product3":400}
mydict["product3"]=500
print(mydict)'''
#Example: reading items from dict using loop

'''mydict={"product1":100,
        "product2":200,
        "product3":400}
mydict["product3"]=500
print(mydict)
for i in mydict:
    print(i) #only prints the keys
for i in mydict:
    print(mydict[i]) #prints only values'''

'''mydict={"product1":100,
        "product2":200,
        "product3":400}
for i in mydict.values():
    print(i) #prints only values
for x, y in mydict.items():
    print(x,y)'''

'''mydict={"product1":100,
        "product2":200,
        "product3":400}
if "product1" in mydict:
    'print("exist")
else:
    print("No")'''
    #OR
'''print("product2" in mydict)'''
#Example.adding and removing items from dict
'''mydict={"product1":100,
        "product2":200,
        "product3":400}
mydict["product4"]=600 #specify the key and value
print(mydict)'''

'''mydict.pop("product2") #Remove product2
print(mydict)'''
#Example: copying dictionary
mydict1={"product1":100,
        "product2":200,
        "product3":400}




mydict2=mydict1.copy()
print(mydict2)



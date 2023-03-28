'''myset={"apple","orange","mangoe"}
print(myset) #output {'mangoe', 'apple', 'orange'}'''

#Example: accessing items from set
'''myset={"apple","orange","mangoe"}

print("apple" in myset) #returns true
print("banana" in myset) #returns false'''

#Example: addding items to set
#add()--->add single item at a time
# update()--->add multiple item at a time

'''myset={"apple","orange","mangoe"}
myset.add("banana")
print(myset)'''

'''myset={"apple","orange","mangoe"}
myset.update(["grapes", "cashew"])
print(myset)'''

#Example: how to remove item using remove(), discard().
'''myset={"apple","orange","mangoe"}
myset.remove("apple")
print(myset)'''

'''myset={"apple","orange","mangoe"}
myset.discard("mangoe")
print(myset)'''
#Example: joining two sets
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)




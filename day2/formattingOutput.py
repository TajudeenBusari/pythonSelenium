name, age, sal="Tajudeen", 30, 1000.67
'''print("Name is:", name)     #In java, we use + sign to join statement together instead of "," here
print("Age is:", age)
print("Salary is:", sal)'''

### Another approach ###

'''print("Name is:%s Age is :%d Salary is :%g" %(name, age, sal))
# %s means string, %d means digit or  number %g means number with decimal'''


### Another approach ###

print("Name is:{} Age is :{} Salary is :{}" .format(name, age, sal))
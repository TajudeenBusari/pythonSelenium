'''global_var=20 #global variable is declared before the function, Can be accessed everywhere

def fun():
    local_var=10   #local variable

    print(local_var)
    print(global_var)
fun()
global_var = 20  # global variable cos it defined outside of the function'''

'''#Example2:
xy=100 #golbal variable
def cool():
    xy=200 #local variable
    print(xy)
cool() #prints 200 and not 100'''

#Example3:using global variable in local variable and update value
'''xy=100 #global variable
def cool():
    global xy
    xy=300 #global variable
    print(xy)
cool() #prints 300'''

'''#Example:
xy=100 #global variable
def cool():
    global xy
    #xy=300 #global variable
    print(xy)
cool()'''

#Example:

def cool():
    global xy
    xy=100
    print(xy) #100
cool()
print(xy) #100



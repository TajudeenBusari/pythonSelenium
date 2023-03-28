'''print("starting here")
print("starting here")
print("starting here")
print("starting here")
print(x) #this will not be executed cos x is not defined anywhere. The program will
#terminate here cos of this and the last one will not be executed
print("ending here here")'''

'''print("starting here")
print("starting here")
print("starting here")
print("starting here")

try:
    print(x)
except:
    print("Exception occured")
print("ending here")'''

#Exmaple:multiple except blocks----try, except else, finally


'''try:
    num1,num2=10,0
    result=num1/num2
    print("result is:",result)
except ZeroDivisionError: #executes only when exception occurs
    print("Thrown ZeroDivisionError exception")
except SyntaxError: #executes only when exception occurs
    print("thrown sysntax error")
except:
    print("Exception handled")
else:
    print("No exception occured") #will only execute if no execption
finally:
    print("always excute") #will block will execute no mattter what'''


#Example4:raising our own exception
def enterage(num):
    if num<0:
        raise  ValueError("Only interger are allowed") #raise is used to throw user defined exception
    if num%2==0:
        print("even")
    else:
        print("odd")

enterage(10) #calling the function and adding the variable
enterage(5)
enterage(-1)

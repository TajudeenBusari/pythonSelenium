#conditional statement
# if  if..else  elif
#Exmaple1: print a person is eligible for vote or not
# age>18 they are eligible

'''age = 20 #take some random  value of age
if age>=18: #end python statement with ":" unlike java ";"
    print("Eligible to vote")
else:
    print("Not Eligible to vote")'''

#Example2: specifying the boolean value directly

'''if False:
    print("true scenerio")
else:
    print("false scenerio")'''
# we can replace the True with 1 or False with 0, it works the same way

#Example3: find wethher a number is even or odd i,2 num%2=0
'''num = 15
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")'''

# Example4: if else in a single line (ternary operator)
'''num = 15
print("Even number") if num%2==0 else print("odd number")'''

# Example5: if else in-multiple statement
'''num = 15
{print("tajudeen"), print ("idowu")} if num>=10 else {print("TJ"), print("ID")}'''

#Exmaple 6: Multiple conditions using elif
weekday=7
if weekday==1:
     print("Monday")
elif weekday==2:
    print("Tuesday")
elif weekday==3:
    print("Wednesday")
elif weekday==4:
    print("Thursday")
else:
    print("invalid week day")










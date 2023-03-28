'''num1=input("Enter first number:")
num2=input("Enter first number:")

#the numbers values can be provided in the console at run time and the those will be stored as string even though we have provided am int

print(type(num1))
print(type(num2))
print(num1 + num2) #gives 100200 (concatenation) bcos it stores the two numbers as string'''
#approach 1 coverts each to int, so plus operator can be applied
'''num1=int(input("Enter first number:"))
num2=int(input("Enter first number:"))

print(type(num1))
print(type(num2))
print(num1 + num2)'''

#approach 2 coverts at the point of addition
num1=int(input("Enter first number:"))
num2=int(input("Enter first number:"))


print(int(num1) +int(num2))

#NB: In the case of decimal numbers, lets say 10.5, use float in place of int
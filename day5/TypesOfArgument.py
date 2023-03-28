#Example1: positional arguments
'''def myfunc(i,j):
    print(i,j)
myfunc(10,20) ##positional arguments

#Example2: keyword
def myfunc(i,j):
    print(i,j)
myfunc(j=10,i=20) ##keyword arguments cos you assign each value'''

'''def func(i, j=10):
    print(i,j)
func(100,200) #return 100, 200
func(100) #returns 100, 10(default value for j)'''

'''def greetings(name, greatmsg):
    print(name+","+greatmsg) #how you want the msg to be conveyed
greetings(name="Tajudeen", greatmsg="hello")'''

#Example:
'''def my_func(a, b, c):
    print(a, b, c)
my_func(10, 20, c=30)
my_func(10,b=20,30) #this will give error cos position arguments must appear before any keyword argument'''
#Example: returning multiple values
def biggest(a, b):
    if a>b:
        return (a,b)
    else:
        return (b,a)

#print(biggest(10,30))
#print(biggest(10,3))
res=biggest(10,30)
print(res)
print(type(res))




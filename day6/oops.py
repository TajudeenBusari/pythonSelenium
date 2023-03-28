
#a function created inside class is a method and by default, it carries one argument self
'''class MyClass:
    def myfunc(self): #first method
        pass #means cos the function is empty
    def display(self, name): #second method
        #print("john")
        print(name)
mc1=MyClass()  #object 1 inside the class which will acquire everything from the class
mc2=MyClass()   #object2 inside the class which will acquire everything from the class

mc1.myfunc() #call the first method with mc1
#mc2.display() #output john #calling the second method with mc1
mc2.display("Tajudeen") #one argument'''

#Example:
'''class MyClas:
    def m1(self): #the self here represent the class
        print("this is instance method")

    @staticmethod     #to create a static method, you have to start with @staticmethod and it is common for every object
    def m2(self, num): #whenever you create a static method, self is also considered as a param, unliike in instance method
        print(self, num)
mc=MyClas() #calling the function directly from the class
mc.m1()
mc.m2(100,200)
MyClas.m2(20,30) #calling the static mehod directly using class and NOT THROUGH OBJCET'''

#EXAMPLE:
'''class MyClass:
    a,b=10,20 #CLASS Variable
    def add(self): #self representing the class in the method
        print(self.a + self.b) #add class to access the class variable

    def mult(self):
        print(self.a * self.b)
mc=MyClass() #creating object for the class
mc.add()
mc.mult()'''

#Example:
'''i,j=15,25 #global variable
class MyClass:
     a,b=10,20 # class variable
     def add(self, x,y): #x, y are local variables
         print(x+y) #x, y are local variable #output 200
         print(self.a+self.b) #a, b are class variable #output 30
         print(i+j) #global variable can be accessed everywhere #output 40
mc=MyClass()
mc.add(100,200)'''
'''#Example
a,b=15,25 #global variable
class MyClass:
     a,b=10,20 # class variable
     def add(self, a,b): #local variable
         print(a+b)
         print(self.a+self.b) #class variables
         print(globals()["a"]+globals()["b"]) #global variable if the name are same

mc=MyClass() #creating object
mc.add(100,200)'''

#Example: multiple objcets for one class

'''class MyClass:
    def display(self, name):
        print("this is display method")
        print(name)
obj1=MyClass() 
obj1.display("Taju") #using objcet to invoke method
obj2=MyClass()
obj2.display("Arigbabuwo")'''

#Example: Constructor
#constructor name is fixed
#constructor can also take argumnets/params
#constructor will be called at the time of object creation

'''class MyClass:
    def __init__(self):
        print("this is constructor")
    def m1(self):
        print("hello")
    def m2(self, x, y):
        return (x+y)
mc=MyClass() #creating object:INVOKES CONSTRUCTOR AUTOMATICALLY, no need for calling method
mc.m1() #method, we have to call explicitly by using objcet



print(mc.m2(2,3))'''

#Example:
'''class MyClass:
    name="Tajudeen" #class variable
    def __init__(self,name): #name is local variable, construvtor expecting one argument
        print(name)
        print(self.name)
mc=MyClass("charles") #passing param to the constructor'''

#Example:
 #constructor: emploiId, name and sal
 #display(): print eid, ename and sal

'''class Emp:
     def __init__(self,eid,ename,sal): #local variable in the constructor
         self.eid=eid
         self.ename=ename
         self.sal=sal
     def display(self): #display is a method which does not print directly, so at the end you have to e1.display()
        print(self.eid, self.ename, self.sal) #for printing purpose we have created another method called display
e1=Emp(100, "Tajudeen", 5000)
e1.display()

e2=Emp(1200, "Arigbabuwo", 3000) #you can add as many methods as possible cos thye are independent of each other
e2.display()'''

#Example:
 #constructor: emploiId, name and sal
 #constructor: print eid, ename and sal

class Emp:
     def __init__(self,eid,ename,sal): #local variable in the constructor
         self.eid=eid
         self.ename=ename
         self.sal=sal
     def __str__(self): #this constructor only returns string type of data, in this case "ename"
        return (self.ename)
e1=Emp(100, "Adegoke", 60000)
print(e1) #print the value of e1 to see 















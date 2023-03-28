# Single inheritance, one parent and one child
'''#Example1:
class A:
    def m1(self):
        print("this is m1 method from class A")
class B(A): #B IS A CHILD OF A
    def m2(self):
        print("this is m2 method from class B")
ObjOfB=B()
ObjOfB.m1()
ObjOfB.m2()
#in this case you are able to access the methods in both class A AND class B THROUGH CREATING AN OBJECT OF B
'''
#Example2:
'''class A:
    X, Y =10,20
    def m1(self):
        print(self.X+self.Y)
class B(A): #CLASS B CONTAINS BOTH VARIABLES AND METHOD OF A IN ADDITION TO ITS OWN, TOTALLY FOUR VARIABLES
    A, B=100,200
    def m2(self):
        print(self.A-self.B)
BObj=B()
BObj.m1()
BObj.m2()'''

'''#Multi-level Inheritance
class A:
    X, Y =10, 20
    def m1(self):
        print(self.X+self.Y)
class B(A):                 #Class B contains the method and variables of A
    A, B = 200, 100
    def m2(self):
        print(self.A + self.B)
class C(B):              #Class C contains the methods and variables of A and B
    i,j = 15, 10
    def m3(self):
        print(self.i-self.j)

#YOU NEED TO CEATE AN OBJECT OF C TO ACCESS EVERYTHING

CObj=C()

CObj.m1()
CObj.m2()
CObj.m3()'''

'''#Hierarchy inheritance
class A:
    X, Y =10, 20
    def m1(self):
        print(self.X+self.Y)
class B(A):                 #Class B contains the method and variables of A
    A, B = 200, 100
    def m2(self):
        print(self.A + self.B)
class C(A):
    i,j = 15, 10
    def m3(self):
        print(self.i-self.j)

#No, relationship between  class B and C

BObj=B()

BObj.m2()
BObj.m1()
CObj=C()
CObj.m3()
CObj.m1()'''

'''#mULTIPLE INHERITANCE: TWO PARENTS FOR ONE SINGLE CHILD
class A:
    X, Y =10, 20
    def m1(self):
        print(self.X+self.Y)
class B:                 #Class B contains the method and variables of A
    A, B = 200, 100
    def m2(self):
        print(self.A + self.B)
class C(A,B):
    i,j = 15, 10
    def m3(self):
        print(self.i-self.j)

CObj=C() #creating an objcet of C
CObj.m1()
CObj.m2()
CObj.m3()
'''

'''#Exmaple: CALLING PARENT CLASS METHOD USING SUPER FUNCTION
class A:
    def method1(self):
        print("method from class A")
class B(A):
    def method1(self):
        print("method from class B") #This is called overriding method cos B has the same method as A, So B will override A
        super().method1() #this will ensure the return of the parent class method through CLASS B
BObj=B()
BObj.method1() #OUTPUT method from class B'''

#Example:
'''class A:
    A, B = 10, 20

class B(A):
    i,j = 100, 200
    def method(self, x, y):
        print(x+y) #local variables
        print(self.i+self.j) #class variable
        print(self.A+self.B) #it is possible to call the variables WITH self from A COS b ´B is a child of A
BObj=B()
BObj.method(500, 1000)'''

#Example.
'''class Parent:
    name="Tajudeen"
class Child(Parent):
    name="John" #Overriding the variable name
    def test(self):
        print(super().name) #this method gets the variable of the parent class
ChildObj=Child()
ChildObj.name
print(ChildObj.name)
ChildObj.test() # OBJECT OF PARENT CLASS THROUGH Child'''

'''class Bank:
    def rateOfInterest(self):
        return 0
class XBank(Bank):
    def rateOfInterest(self):
        return 5
class YBank(Bank):
    def rateOfInterest(self):
        return 7
ObjOfXBank=XBank()
ObjOfXBank.rateOfInterest()
print(ObjOfXBank.rateOfInterest()) #5

ObjOfYBank=YBank()
ObjOfYBank.rateOfInterest()
print(ObjOfYBank.rateOfInterest()) #7'''


#Example: overloading concept(polymorphism)
#1
'''class Human:
    def SayHello(self, name=None): #if you dont pass any param, it is going to none
        if name is not None:
            print("Hello  "+name)
        else:
            print("Hello")
ObjectOfHuman=Human()
ObjectOfHuman.SayHello("Tajudeen") #Output Hello  Tajudeen
ObjectOfHuman.SayHello() #Hello'''

#2
class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)
ObjOfCal=Calculation()
ObjOfCal.add() #0
ObjOfCal.add(20,30) #50
ObjOfCal.add(20,30,40) #90
































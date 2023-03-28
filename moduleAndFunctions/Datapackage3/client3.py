import sys
sys.path.append("//moduleAndFunctions/DataPackage1")
sys.path.append("//moduleAndFunctions/DataPackage2")
#Approach1
'''import emp
empObj=emp.Employee(101, "TAJU", 200000)
empObj.displayemp()

import stu
stuObj=stu.Student(100, "IDOWU", "A")
stuObj.displaystu()'''
#Approach2
#if you dont wamt to specify the module name everytime
from emp import Employee
empObj=Employee(100, "TJ", 3000)
empObj.displayemp()
#do same for student
from stu import Student

stuObj=Student(300, "Femi", 15 )
stuObj.displaystu()


#Approach1

#accessing module 1 which is inside pack 1,
# we cant access directly cos they are not in the same directory
'''import sys
sys.path.append("C:/Users/tajudeen.busari/pythonProject/pythonSelenium/moduleAndFunctions/pack1")
#Module1 is present in pack1
sys.path.append("C:/Users/tajudeen.busari/pythonProject/pythonSelenium/moduleAndFunctions/pack1/pack2")
#Module2 is present in pack2
import module1
import module2


module1.display()
module2.show()'''

#Approach2
import sys
sys.path.append("//moduleAndFunctions/pack1")
#Module1 is present in pack1
sys.path.append("//moduleAndFunctions/pack1/pack2")
#Module1 is present in pack2
from module1 import *
from module2 import *
display()
show()


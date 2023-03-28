import sys
sys.path.append("//moduleAndFunctions/package1")
#Approach1

'''import module1
import module2


module1.display()
module2.show()'''

#Approach2

from module1 import *
from module2 import *


display() #just call the method directlu
show()

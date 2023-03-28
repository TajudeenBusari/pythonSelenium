#Approach 1
'''import a
import b
AnimalObj=a.Animal() #Objct from Animal module----->a
AnimalObj.display()

BirdObject=b.Bird() #Objct from Bird module----->b
BirdObject.display()'''

#Approach 2
from a import Animal
from b import Bird
AnimalObj=Animal()
AnimalObj.display()


BirdObject=Bird()
BirdObject.display()
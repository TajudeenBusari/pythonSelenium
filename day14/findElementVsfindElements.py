from selenium import webdriver
from selenium.webdriver.common.by import By
import time
webdriver.Chrome()
driverObj=webdriver.Chrome()
driverObj.get("https://www.mirasys.com/")
#          find_element() return single web element
#1: locator matching with single web element
'''driverObj.find_element(By.XPATH, "//input[@id='input_search-box-input-comp-kb0ysa1p']")
element=driverObj.find_element(By.XPATH, "//input[@id='input_search-box-input-comp-kb0ysa1p']")
element.send_keys("VMS")
time.sleep(3)'''


#2: locator matching with multiple web element
'''driverObj.find_element(By.XPATH, "//div[@class='CJF7A2']//a" ) #this locator matches 19 elements. This will only the first element of the 19
element=driverObj.find_elements(By.XPATH, "//div[@class='CJF7A2']//a" )
#print(element.text) #list has no attribute text here, you can use another example
print(len(element)) #Output 19'''

#3: elemnet not availbele then throw NOSuchElementException

#subMit=driverObj.find_element(By.XPATH, "//button[@class='kuTaGy zKbzSQ']")
'''subMit=driverObj.find_element(By.XPATH, "//button[@class='kuTaGy ']") #alterring locator, gives Noexcepton error
subMit.click()'''
#### find elements()-Return multiple webElement. FInd elements always return list collection/object


#1 Locator matching with single webElement
'''driverObj.find_elements(By.XPATH, "//input[@id='input_search-box-input-comp-kb0ysa1p']")#this returns a single web element in list form
elements=driverObj.find_elements(By.XPATH, "//input[@id='input_search-box-input-comp-kb0ysa1p']")
print(len(elements)) #output 1
print(elements[0].text) #this the way to print elements in list form
print(elements[0].send_keys("VMS")) #only this we can pass value into the element
time.sleep(3)'''



#2 Locator matching with multiple webElements
'''driverObj.find_element(By.XPATH, "//div[@class='CJF7A2']//a" )
elements=driverObj.find_elements(By.XPATH, "//div[@class='CJF7A2']//a" )
print(len(elements))
#print(elements[0].text) #output ABOUT US
for ele in elements: #ele is just a varaible
    print(ele.text) #prints all elements in the list'''
#OUTPUT
'''ABOUT US
MIRASYS VMS
HARDWARE
INTEGRATION
REFERENCES
NEWS
PRIVACY POLICY
TERMS OF USE
SUPPORT & TRAINING
EXTRANET
DOCUMENTATION
EVENTS
BE A PARTNER
CONTACT US
info@mirasys.com
GET A DEMO'''
#3 Element not available will return 0 instead of No exception error witnessed in find_element











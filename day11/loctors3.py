from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driverObj=webdriver.Chrome()
driverObj.get("https://www.facebook.com/")
driverObj.maximize_window() #always do this to see all elements on the web page


#1 tag & id: should folow this syntax 'tagname#valueofId'. Th word tag is always option i.e #valueofid
#driverObj.find_element(By.CSS_SELECTOR, "input#email").send_keys("tajudeen.busari10@gmail.com")

'''#2 tag&class: tagname.valueofclass or .valueofclass
driverObj.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("tajudeen.busari10@gmail.com")
#'.inputtext _55r1 _6luy', for this locator, remove all the part after the space so that it can be located
time.sleep(5)'''#even though the locator also matches the second element password, it will only work for email cos
#we use find element and not elements

#3 tag&attribute: tagname[attribute=value], any attribute
'''driverObj.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("tajudeen.busari10@gmail.com")
time.sleep(3)'''

#4 tag, class & attribute: tagname.valueofClass[attribute=value]
driverObj.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("xyz") #this for the password box
time.sleep(3)



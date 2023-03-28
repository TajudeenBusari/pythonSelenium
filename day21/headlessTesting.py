import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def headless_chrome(): #creating function
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driverObj=webdriver.Chrome(options=ops) #object placed in a variable
    return driverObj
driverObj=headless_chrome() #calling the unction uising the variable returned

driverObj.get("https://www.mirasys.com/")
print(driverObj.title)
print(driverObj.current_url)
driverObj.close()

#same can be done for edge and firefox
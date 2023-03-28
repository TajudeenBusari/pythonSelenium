from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driverObj=webdriver.Edge() ##creating obj for the weddriver class
driverObj.get("https://www.magictoolbox.com/magicslideshow/examples/") #i just google this website and got it
driverObj.maximize_window()
driverObj.find_elements(By.TAG_NAME,"a")
links=driverObj.find_elements(By.TAG_NAME,"a") #every link on a web page ahas anchor tag "a"
print(len(links)) #output 149 #same thimg can be done for slides as well





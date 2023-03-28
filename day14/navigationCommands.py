from selenium import webdriver
from selenium.webdriver.common.by import By
import time
webdriver.Chrome()
driverObj=webdriver.Chrome()
driverObj.get("https://www.mirasys.com/")
driverObj.get("https://www.netflix.com/fi-en/")

driverObj.back() #this method goes back to the previous page(mirasys)
driverObj.forward()  #this method goes forward to forward  page(netflix)
driverObj.refresh() #this method goes refreshes to current  page(netflix)
time.sleep(4)



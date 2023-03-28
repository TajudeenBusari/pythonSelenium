from selenium import webdriver
from selenium.webdriver.common.by import By
import time
webdriver.Chrome()
driverObj=webdriver.Chrome()
driverObj.get("https://www.mirasys.com/")


print(driverObj.title) #out put 'Mirasys VMS - Open Video Management System | Finland'
print(driverObj.current_url)
print(driverObj.page_source) #this captures the source code of the web page
driverObj.close()
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driverObj=webdriver.Chrome()
driverObj.implicitly_wait(2)
driverObj.get("https://www.mirasys.com/")
driverObj.maximize_window()
#driverObj.save_screenshot("C:\\Users\\tajudeen.busari\\pythonProject\\pythonSelenium\\day21\\mirasysHomePage.png")
            #OR
#driverObj.save_screenshot(os.getcwd()+"mirasysHomePage.png")
#driverObj.get_screenshot_as_file(os.getcwd()+"mirasysHomePage.png")

driverObj.get_screenshot_as_base64() #save in binary concept
driverObj.get_screenshot_as_png() #save in binary concept
#you can provide the location you want to save your screen shot

time.sleep(3)
driverObj.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
webdriver.ChromeOptions()
ops=webdriver.ChromeOptions() #this object inside the variable ops is used to disbale any kind of pop up when opening a browser
ops.add_argument("--disable-notifications")


webdriver.Chrome()
webDriverObj=webdriver.Chrome()
webDriverObj.get("https://whatmylocation.com/")
webDriverObj.maximize_window()

time.sleep(4)


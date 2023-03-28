import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("url")
webdriverObj.maximize_window()
button=webdriverObj.find_element(By.XPATH, "xpath of the element to be double clicked")
act=ActionChains(webdriverObj)
act.double_click(button).perform() #double click action
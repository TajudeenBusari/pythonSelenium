from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("url")
webdriverObj.maximize_window()

source_element=webdriverObj.find_element(By.XPATH, "xpath of the element to be dragged") #what you r dragging
target_element=webdriverObj.find_element(By.XPATH, "xpath of the element to be to be dragged on") #where you are dragging to


act=ActionChains(webdriverObj)
act.drag_and_drop(source_element, target_element).perform() #drag and drop
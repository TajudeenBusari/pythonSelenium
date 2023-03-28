import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
webdriverObj.maximize_window()
webdriverObj.implicitly_wait(3)
button=webdriverObj.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(webdriverObj)
act.context_click(button).perform() #right click
time.sleep(2)




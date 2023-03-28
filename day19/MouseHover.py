import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://www.mirasys.com/")
webdriverObj.maximize_window()
time.sleep(3)

#product-->integration-->references
product=webdriverObj.find_element(By.XPATH, "//p[@id='comp-ioclk9190label']")
integration=webdriverObj.find_element(By.XPATH, "//p[@id='comp-ioclk9191label']")
references=webdriverObj.find_element(By.XPATH, "//p[@id='comp-ioclk9192label']")

act=ActionChains(webdriverObj) #import actionchain module from class selenium webdriver
act.move_to_element(product).move_to_element(integration).move_to_element(references).click().perform()
#you must use perform to action to be carried out
time.sleep(3)


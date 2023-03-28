from selenium import webdriver
from selenium.webdriver.common.by import By
import time
webdriver.Chrome()
driverObj=webdriver.Chrome()
driverObj.get("https://www.mirasys.com/")
driverObj.maximize_window()
driverObj.find_element(By.XPATH, "//div[@id='comp-ld8h0zes']").click()
time.sleep(5)
#driverObj.close() #this only closes the focused or parent browser window and not the child
driverObj.close() #this only closes all windows, closes all browser processes


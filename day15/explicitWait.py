
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

webdriver.Chrome()
driverObj=webdriver.Chrome()
wait=WebDriverWait(driverObj, 10, poll_frequency=2, ignored_exceptions=[Exception]) #IMPORT THE WebDriverWait MODULE
driverObj.get("https://www.google.com/")
driverObj.find_element(By.XPATH, "//div[@class='QS5gu sy4vM']").click() #WILL CLICK THE ACCEPTANCE BUTTON
#time.sleep(3) ##i put this to click on the acceptance agreement
driverObj.maximize_window()
driverObj.find_element(By.NAME, "q")
searchBox=driverObj.find_element(By.NAME, "q")
searchBox.send_keys("Selenium")
searchBox.submit()
SearchLink=wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']"))) #import the EC (Exception condition module)
SearchLink.click()

#this method is more effective but you have to write in many places if there are many exception
#we dont use find method here cos it is already happening in the wait module
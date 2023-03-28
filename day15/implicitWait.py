from selenium import webdriver
from selenium.webdriver.common.by import By
import time
webdriver.Chrome()
driverObj=webdriver.Chrome()
#driverObj.implicitly_wait(10) #unless, dtiverObj process is killed, the implicit wait will take care of any synchronisation probrlm
driverObj.get("https://www.google.com/")
driverObj.find_element(By.XPATH, "//div[@class='QS5gu sy4vM']").click() #WILL CLICK THE ACCEPTANCE BUTTON
time.sleep(3) ##i put this to click on the acceptance agreement
driverObj.maximize_window()
driverObj.find_element(By.NAME, "q")
searchBox=driverObj.find_element(By.NAME, "q")
searchBox.send_keys("Selenium")
searchBox.submit()
driverObj.find_element(By.XPATH, "//h3[text()='Selenium']").click()



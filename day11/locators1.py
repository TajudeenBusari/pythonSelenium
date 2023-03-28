from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driverObj=webdriver.Edge() ##creating obj for the weddriver class
driverObj.get("https://www.netflix.com")          #https://demo.nopcommerce.com/
driverObj.maximize_window()
time.sleep(3)
driverObj.find_element(By.LINK_TEXT, "Sign In").click()
driverObj.find_element(By.NAME, "userLoginId").send_keys("tajudeen.busari10@gmail.com")
driverObj.find_element(By.ID, "id_password").send_keys("gauss1234567")
driverObj.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()
time.sleep(3)
#driverObj.close() #to cls browser
#driverObj.quit() #to quit
#driverObj.find_element(By.PARTIAL_LINK_TEXT, "Sign")
#driverObj.find_element(By.NAME, "email").send_keys("tajudeen.busari10@gmail.com")
#driverObj.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/div/form/div/button').click()
#time.sleep(3)


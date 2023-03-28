import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driverObj=webdriver.Chrome()
driverObj.get("https://www.foundit.in/")
driverObj.maximize_window()
driverObj.find_element(By.XPATH, "//div[@class='heroSection-buttonContainer_secondaryBtn__text']").click()
driverObj.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("C:\\Users\\Recommendation_letter.pdf")

time.sleep(4)
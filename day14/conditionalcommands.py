from selenium import webdriver
from selenium.webdriver.common.by import By
import time
webdriver.Chrome()
driverObj=webdriver.Chrome()
driverObj.get("https://www.mirasys.com/")
driverObj.maximize_window()
searchBox=driverObj.find_element(By.XPATH, "//input[@id='input_search-box-input-comp-kb0ysa1p']") #this captures the web element

#1. is_displayed
searchBox.is_displayed() #a method used to confirm if the element is displayed

print("status is displayed:", searchBox.is_displayed())
#expected: true or false

#2. is_enabled
searchBox.is_enabled() #a method used to confirm if the element is enabled

print("status is enabled:", searchBox.is_enabled())
#expected: true or false

#3. is_selected(): used for radio button and check boxes
driverObj.find_element(By.XPATH, "//input[@value='checked']")
checkBox=driverObj.find_element(By.XPATH, "//input[@value='checked']")
checkBox.is_selected() #a method used to confirm if the checkbox is selected

print("status is:", checkBox.is_selected())
#expected: true or false

checkBox.click() #this method clicks the check box
print(checkBox.is_selected())
#expected: true

driverObj.quit()



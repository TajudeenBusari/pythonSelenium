import time

from selenium import webdriver
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://opensource-demo.orangehrmlive.com/")
webdriverObj.maximize_window()
time.sleep(2)

webdriverObj.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
webdriverObj.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
webdriverObj.find_element(By.XPATH, "//button[@type='submit']").click()


webdriverObj.find_element(By.XPATH, '//li[1]//a[1]//span[1]').click() #there is a problrm with the xpath

webdriverObj.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
webdriverObj.find_element(By.XPATH, "//a[@role='menuitem']").click()

count=0
rows=len()
print("total number of row in the table:", rows)
for r in range(1, rows+1):
    status=webdriverObj.find_elements(By.XPATH, "").text
    if status=="Enabled":
        count=count+1
print("total no of rows in a table: ", rows)
print("total no of Enabled users: ", count)
print("total no of disabled user: ", rows)





time.sleep(3)


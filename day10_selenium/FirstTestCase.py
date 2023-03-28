#Test Case
# 1. Open webbrowser
#2. Open url https://opensource-demo.orangehrmlive.com/
#3. Enter Username #Admin
#4. Enter password #admin123
#5.click on login
#6. capture tittle of the home page (actual)
#7. verify the tittle of the home page (Expected)
#8. close browser


#WebDriver is module available in selenium package

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#serviceObj=Service("C:\\Users\\tajudeen.busari\\Drivers\\chromedriver_win32\\chromedriver.exe")
ChromeDriverObj=webdriver.Chrome()
#ChromeDriverObj=webdriver.Chrome(service=serviceObj)
ChromeDriverObj.get("https://opensource-demo.orangehrmlive.com/") #this site has some issues or anothet page is launching befre ot opens , so the element is not detected right

ChromeDriverObj.find_element(By.XPATH,"//input[@name='username']" ).send_keys("Admin")
'''ChromeDriverObj.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys("admin123")
ChromeDriverObj.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

actual_tittle=ChromeDriverObj.title
expect_tittle="OrangeHRM"
if actual_tittle==expect_tittle:
    print("log in test passed")
else:
    print("login failed")
ChromeDriverObj.close()'''
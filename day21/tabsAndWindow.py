import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driverObj=webdriver.Chrome()
driverObj.implicitly_wait(2)


'''driverObj.get("https://demo.nopcommerce.com/")
driverObj.maximize_window()
getADemo=Keys.CONTROL+Keys.RETURN
driverObj.find_element(By.LINK_TEXT, "Register").send_keys(getADemo) #this willl open the get a testFrameWorkDemo page in another tab
#BUT WILL NOT SWITCH TO THE SECOND TAB, THIS IS DIFFRENT IN SELENIUM 4'''

#New Tab-selenium 4: opens a new tab and switch to it

'''driverObj.get("https://demo.nopcommerce.com/")
driverObj.switch_to.new_window("tab")#open another tab for the following url
driverObj.get("https://www.mirasys.com/")'''

#New window-selenium4. open a new window and swiches t new window

driverObj.get("https://demo.nopcommerce.com/")
driverObj.switch_to.new_window("window")#open another window for the following url
driverObj.get("https://www.mirasys.com/")






time.sleep(3)


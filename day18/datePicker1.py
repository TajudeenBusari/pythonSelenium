import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
webdriverObj.maximize_window()
webdriverObj.find_element(By.XPATH, "//input[@id='dob']").click()
#select the dropdown element for month
webdriverObj.find_element(By.XPATH, "//select[@aria-label='Select month']")
#use select class for the drop down menu and import the class
date_picker_month=Select(webdriverObj.find_element(By.XPATH, "//select[@aria-label='Select month']"))
date_picker_month.select_by_visible_text("Jan")


#select the dropdown element for year
webdriverObj.find_element(By.XPATH, "//select[@aria-label='Select year']")
#use select class for the drop down menu and import the class
date_picker_year= Select(webdriverObj.find_element(By.XPATH, "//select[@aria-label='Select year']"))
date_picker_year.select_by_visible_text("1999")


webdriverObj.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
allDates=webdriverObj.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in allDates:
    if date.text=="17":
        date.click()
        break
        
time.sleep(4)





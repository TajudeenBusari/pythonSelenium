import time

from selenium import webdriver
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://jqueryui.com/datepicker/")
webdriverObj.maximize_window()
time.sleep(3)
webdriverObj.switch_to.frame(0) #switch to frame #only one frame the first one

#approach1
#webdriverObj.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys("03/01/2021") #mm/dd/yyyy


#approach2
year="2022"
month="April"
date="15"
webdriverObj.find_element(By.XPATH, '//*[@id="datepicker"]').click()
#immediately after clicking, capture the year and month and compare with the expected value above
#next click on the arrow mark until the year and month matches
#since we donr know how many times we have to click until we get expected result, we use while loop

while True:
    mon=webdriverObj.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text #captures the month text
    yr=webdriverObj.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if month==mon and year==yr:
        break;
    else:
        #webdriverObj.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click() #next arrow
        webdriverObj.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click() #previous arrow

#select date
#first write xpath for the date table = "//table[@class='ui-datepicker-calendar']"
#add the body to it cos the data we want to capture is inside the tbody = //table[@class='ui-datepicker-calendar']/tbody
#"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a" gives all dates
dates=webdriverObj.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break





time.sleep(3)

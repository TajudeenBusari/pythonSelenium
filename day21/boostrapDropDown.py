#in this case we cant use select class cos the options are boostrap

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driverObj=webdriver.Chrome()
driverObj.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driverObj.maximize_window()
driverObj.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click() #performs click action and open up the other options(elemnets)
countries=driverObj.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li") #THIS GETS THE LISTS OF ALL COUNTRIES
print(len(countries)) #249
#write a loop statement to select specific country
for country in countries:
    if country.text=="Nigeria": #since country is a text
        country.click() #country is also a web element, we can click
        break


time.sleep(3)

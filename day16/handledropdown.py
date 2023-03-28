import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

webdriver.Chrome()
webdriverOBJ=webdriver.Chrome()
webdriverOBJ.get("https://www.opencart.com/index.php?route=account/register")
webdriverOBJ.maximize_window()
webdriverOBJ.find_element(By.XPATH, "//select[@name='country_id']")
countryDropDownElemt=webdriverOBJ.find_element(By.XPATH, "//select[@name='country_id']")
dropDownCountry=Select(countryDropDownElemt) #import the select class

#diffrent ways of selecting
#dropDownCountry.select_by_visible_text("Nigeria")
#dropDownCountry.select_by_value("10")
#dropDownCountry.select_by_index(11)




#capture all options and print them
allOptions=dropDownCountry.options #option is used to slect option element and store in variavle allOptions
print("total number of countries is:", len(allOptions)) #242

'''for countries in allOptions:
    print(countries.text)'''

#select options from dropdown without built in function

'''for country in allOptions:
    if country.text=="Nigeria":
        country.click()
        break'''
#without using the select class
#just copy the option xpath on the webpage and use direectly




time.sleep(4)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver.Chrome()
webdriverOBJ=webdriver.Chrome()
webdriverOBJ.get("https://itera-qa.azurewebsites.net/home/automation")
webdriverOBJ.maximize_window()
'''#1 select specific cehckbox
webdriverOBJ.find_element(By.XPATH, "//input[@id='monday']").click()'''
#2 select all check boxes
webdriverOBJ.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
checkBoxes=webdriverOBJ.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkBoxes)) #output 7

#Approach1
'''for i in range (len(checkBoxes)):
    checkBoxes[i].click()'''
#Approach2
'''for checkbox in checkBoxes:
    checkbox.click()
'''

#Approach3 select multiple checkboxes by choice
'''for checkbox in checkBoxes:
    weekday=checkbox.get_attribute("id") #get the value of the attribute which are the days and store in variable weekday
    if weekday=="monday" or weekday=="sunday":
        checkbox.click()'''

#Approach4 last two checkboxes
#range(5,7)--->6,7
#total num of elements-2=starting index
'''for i in range(len(checkBoxes) - 2, len(checkBoxes)):
    checkBoxes[i].click()'''

#Approach5 first two check boxes
'''for i in range(len(checkBoxes)):
    if i<2:
        checkBoxes[i].click()'''

#Approach6
for checkbox in checkBoxes:
    if checkbox.is_selected():
        checkbox.click()






time.sleep(3)




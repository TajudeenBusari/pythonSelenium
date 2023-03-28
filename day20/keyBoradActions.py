#CTRL A
#
#
#

import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://text-compare.com/")
webdriverObj.implicitly_wait(10)
webdriverObj.maximize_window()

input1=webdriverObj.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2=webdriverObj.find_element(By.XPATH, "//textarea[@id='inputText2']")
input1.send_keys("welcome tajudeen")
act=ActionChains(webdriverObj)

#input1---> ctrl+A SELECT THE TEXT
act.key_down(Keys.CONTROL) #press control key board
act.send_keys("a") #press A key board
act.key_up(Keys.CONTROL) #Release the contl key board
act.perform() #perform the action
#you can write all the statemnet above in a single line with . in between

#input1 contrl+c copy text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#press tab key to move to the second input box
act.send_keys(Keys.TAB).perform()

time.sleep(3)

#input2---->Ctrl+V paste the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


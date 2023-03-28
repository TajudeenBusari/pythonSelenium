from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver.Chrome()
webdriverOBJ=webdriver.Chrome()
webdriverOBJ.get("https://demo.nopcommerce.com/")
webdriverOBJ.maximize_window()
#click on links
webdriverOBJ.find_element(By.LINK_TEXT, "Digital downloads").click()
#printing all links name
links=webdriverOBJ.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text) #use .text cos link is a web element

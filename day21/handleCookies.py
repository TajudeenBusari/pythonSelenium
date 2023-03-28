
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driverObj=webdriver.Chrome()
driverObj.implicitly_wait(10)
driverObj.get("https://www.mirasys.com/")
driverObj.maximize_window()

#captures cookies from the browser
#cookies have attributes and values--->name="xyz", value=1234, expirydate=1.1.2022 whch sholub be stored in a dict
cookies=driverObj.get_cookies()
print("size of cookies:",len(cookies)) #5

#print details of all cookies

'''for c in cookies:
    #print(c)
    print(c.get("name"),":", c.get("value"))'''
#Add new cookies to the browser
'''driverObj.add_cookie({"name":"taju", "value":"12345"})
cookies=driverObj.get_cookies() # you must capture b4 any further action
print("size of cookies after adding one:", len(cookies)) #6'''

#delete specific cookie from the browser
'''driverObj.delete_cookie("taju")
cookies=driverObj.get_cookies()
print("size of cookies after adding one:", len(cookies))'''

#delete all cookies from the browser
driverObj.delete_all_cookies()
cookies=driverObj.get_cookies()
print("size of cookies after deletion:", len(cookies))



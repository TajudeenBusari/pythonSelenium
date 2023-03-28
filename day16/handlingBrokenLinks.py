#a broken link is the one that does not have any target page, they give a error response
#400>= response code is broken link
#<400 is normal link
#first import requests package

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests


webdriver.Chrome()
webdriverOBJ=webdriver.Chrome()
webdriverOBJ.get("http://www.deadlinkcity.com/")
webdriverOBJ.maximize_window()
allLinks=webdriverOBJ.find_elements(By.TAG_NAME, "a")

countallLinks=0
for link in allLinks:
    link.get_attribute("href") #this gets the attribute of each href which is a url(variable)
    url=link.get_attribute("href") #store it in a variable url
    try: #put the requests in try, except block in case of any delay in response to avoid any error
        requests.head(url) #making a request to the url with the help of the module requests
        res=requests.head(url) #store in a variable
    except:
        None

    if res.status_code>=400:
        print(url,"    is broken" )
        countallLinks+=1 #increase each count by 1 everytime until the last
    else:
        print(url,"    is valid link")
print("total number of broken links is:", countallLinks)






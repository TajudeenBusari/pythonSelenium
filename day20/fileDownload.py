import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()  # THIS WILL ENABLE DOWNLOADING INTO CURRENT/working DIRECTORY


def chrome_setup():  # we have created this set up function so that we can call another browser by just calling the function. This time it is chrome
    from selenium.webdriver.chrome.service import Service
    serObj = Service("C:\\Users\\tajudeen.busari\\Drivers\\chromedriver_win32\\chromedriver.exe")
    # download file in the desired location
    preferences = {"download.default_directory": location}  # IT IS GOING TO DOWNLOAD INTO OUR desired DIRCTORY FOLDER
    ops = webdriver.ChromeOptions()  # We use this class from webdriver module then store it in a variable
    ops.add_experimental_option("prefs", preferences)

    webdriverObj = webdriver.Chrome(service=serObj, options=ops)  # pass the ops into the chrome webdriver
    return webdriverObj  # object instance return

''''def Edge_setup():  # we have created this set up function so that we can call another browser by just calling the function. This time it is chrome
    from selenium.webdriver.edge.service import Service
    serObj = Service("C:\\Users\\tajudeen.busari\\Drivers\\edgedriver_win64\\msedgedriver.exe")
    # download file in the desired location
    preferences = {"download.default_directory": location}  # IT IS GOING TO DOWNLOAD INTO OUR desired DIRCTORY FOLDER
    ops = webdriver.EdgeOptions()  # We use this class from webdriver module then store it in a variable
    ops.add_experimental_option("prefs", preferences)

    webdriverObj = webdriver.Edge(service=serObj, options=ops)  # pass the ops into the chrome webdriver
    return webdriverObj  # object instance return'''

'''def Edge_setup():

    preferences={"download.default_directory": location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    webEdgedriverObj= webdriver.Edge(options=ops)
    return webEdgedriverObj'''

#works well
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj=Service("C:\\Users\\tajudeen.busari\\Drivers\\geckodriver-v0.32.2-win64\\geckodriver.exe.")
    #settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword") #for msword download, you can do sme for other file type
    #check mime type for diffrent document files https://www.sitepoint.com/mime-types-complete-list/, ctrl+F to find (for e.g .txt)
    ops.set_preference("browser.download.manager.showWhenStarting", False) #the pop up window will not appear on the browser
    ops.set_preference("browser.download.folderList", 2) #0--desktop, 1--download folder, 2--desired location e.g directory
    ops.set_preference("browser.download.dir", location)
    webFirefoxDriverObj= webdriver.Firefox(service=serv_obj, options=ops)
    return webFirefoxDriverObj




#webdriverObj = chrome_setup()
#webEdgedriverObj=Edge_setup()
webFirefoxDriverObj=firefox_setup()
time.sleep(2)

webFirefoxDriverObj.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
webFirefoxDriverObj.maximize_window()

webFirefoxDriverObj.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

time.sleep(10)

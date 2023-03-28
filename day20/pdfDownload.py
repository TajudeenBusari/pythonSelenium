import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()  # THIS WILL ENABLE DOWNLOADING INTO CURRENT/working DIRECTORY

#works well
def Chrome_setup():

    preferences={"download.default_directory": location, "plugins.always_open_pdf_externally":True}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driverObj= webdriver.Chrome(options=ops)
    return driverObj


#works well
def Edge_setup():

    preferences={"download.default_directory": location, "plugins.always_open_pdf_externally":True} #has open bug, so edge doesnt work, it will just open it and not dowmnload
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)
    driverObj= webdriver.Edge(options=ops)
    return driverObj

#works well
def Firefox_setup():

    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True ) #for pdf
    driverObj= webdriver.Firefox(options=ops)
    return driverObj


#driverObj = Chrome_setup()
#driverObj = Edge_setup()
driverObj = Firefox_setup()
time.sleep(2)

driverObj.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driverObj.maximize_window()

driverObj.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()

time.sleep(10)
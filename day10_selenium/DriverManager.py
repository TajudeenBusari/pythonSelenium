#https://pypi.org/project/webdriver-manager/ Find the documentation here
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driverObj = webdriver.Chrome(ChromeDriverManager().install())

driverObj.get("https://www.google.com/")
driverObj.maximize_window()
time.sleep(3)
driverObj.close()


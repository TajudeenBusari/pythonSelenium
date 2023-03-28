from selenium import webdriver
from selenium.webdriver.common.by import By
import time
WebDriverOBJ=webdriver.Chrome()
WebDriverOBJ.get("https://www.netflix.com/fi-en/")
WebDriverOBJ.maximize_window()
#contains() and start-with()
WebDriverOBJ.find_element(By.XPATH,'//*[@id="73e2dc92a19c3"]').send_keys("tajudeen.busari10@gmail.com")
WebDriverOBJ.find_element(By.XPATH,"//button[starts-with(@data-uia,'our-story-cta-hero_fuji')]" ).click()
time.sleep(4)
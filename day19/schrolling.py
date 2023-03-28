import time

from selenium import webdriver


from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
webdriverObj.maximize_window()
#since this schrolling action isnt in our application, it is on the browser, we cant use the ChainAction class

#1. scroll down page ny pixel
'''webdriverObj.execute_script("window.scroll(0, 3000)", "") #window.scroll id a js function. we moving from 0 to 3000
value=webdriverObj.execute_script("return window.pageYOffset;") #gets/prints the location of the final destination. the movemnet is y axis
print("Number of pixel moved:", value) #OUTPUT 3000'''

#2. scroll down page till elemnet is visible
'''webdriverObj.find_element(By.XPATH, "//img[@alt='Flag of Nigeria']")
flag=webdriverObj.find_element(By.XPATH, "//img[@alt='Flag of Nigeria']")
webdriverObj.execute_script("arguments[0].scrollIntoView();", flag) #Nigeria flag
value=webdriverObj.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value) #output 1897.3333740234375'''

#3. scroll down the page till end

webdriverObj.execute_script("window.scrollBy(0, document.body.scrollHeight)", "") #the excute is cos of the js function wr are using
value=webdriverObj.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value) #output 5737.33349609375

time.sleep(4)

#4. scroll up  the page till initial postion
webdriverObj.execute_script("window.scrollBy(0, -document.body.scrollHeight)", "")
value=webdriverObj.execute_script("return window.pageYOffset;")
print("Number of pixel moved:", value) #output  0


time.sleep(2)





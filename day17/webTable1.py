#1 count number of row and coloumn
#2 read specific row and coloumn
#3 read all the rows and coloumn
#4 read data based on condition(list books name whose author is Mukesh)
#

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://testautomationpractice.blogspot.com/")

#1 count number of row and coloumn
webdriverObj.maximize_window()
'''noOfRow=len(webdriverObj.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")) #we are not specifying any index, so it captures all rows
noOfColums=len(webdriverObj.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))#we are not specifying any index, so it captures all columns
print(noOfRow) #7
print(noOfColums) #4
webdriverObj.close()'''

#2 read specific row and coloumn
'''data=webdriverObj.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data) #output Master In Selenium'''

#3 read all the rows and coloumn
'''noOfRow=len(webdriverObj.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
noOfColums=len(webdriverObj.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))
for r in range(2, noOfRow+1): #add +1 cos the function wont count the last one
    for c in range(1, noOfColums+1): #add +1 cos the function wont count the last one
        data=webdriverObj.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
            #pass the r and c dynamically and convert them to string then add + before and after to be able to capture all rows and column
        print(data, end="        ")
    print() #this will ensure it is printed in table form as it is in the webpage'''




#4 read all the rows and coloumn
noOfRow=len(webdriverObj.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
noOfColums=len(webdriverObj.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))
for r in range(2, noOfRow+1): #starting from second row
    #column value is a constant, we dont need to pass dynamically
    authorName=webdriverObj.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookName=webdriverObj.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        print(bookName, "       ", authorName)

#Output
#Learn Java         Mukesh
#Master In Selenium         Mukesh



time.sleep(2)
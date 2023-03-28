import time
from selenium import webdriver
from pythonSelenium.day22 import ExcelUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#this code works although with this website example, a pop up may cause the failure

driverObj=webdriver.Chrome()

driverObj.implicitly_wait(3)
driverObj.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driverObj.maximize_window()
time.sleep(20)

file="C:\\Users\\tajudeen.busari\\cameraSettings.xlsx"
rows=ExcelUtils.getRowCount(file, "Sheet4") #gives the number of row available in the excel sheet
for r in range(2, rows+1):
    principal=ExcelUtils.readData(file, "Sheet4", r, 1)
    RateOfInterest=ExcelUtils.readData(file, "Sheet4", r, 2)
    Per1 = ExcelUtils.readData(file, "Sheet4", r, 3)
    Per2= ExcelUtils.readData(file, "Sheet4", r, 4)
    Freq = ExcelUtils.readData(file, "Sheet4", r, 5)
    Exp_mVlaue=ExcelUtils.readData(file, "Sheet4", r, 6) #in string string format (text)

    #passing the data to the application
    driverObj.find_element(By.XPATH, "//input[@id='principal']").send_keys(principal)
    driverObj.find_element(By.XPATH, "//input[@id='interest']").send_keys(RateOfInterest)
    driverObj.find_element(By.XPATH, "//input[@id='tenure']").send_keys(Per1)
    periodDropDown=Select(driverObj.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    periodDropDown.select_by_visible_text(Per2)
    freqDropDown=Select(driverObj.find_element(By.XPATH, "//select[@id='frequency']"))
    freqDropDown.select_by_visible_text(Freq)
    driverObj.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click() #calculate button
    Act_mValue=driverObj.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text  #in string format text

    #validation
    #to comapre  Exp_mVlaue and act_mValue, convert thme to number (float)
    if float(Exp_mVlaue)==float(Act_mValue):
        print("test passed")
        ExcelUtils.writeData(file, "Sheet4", r, 8, "pass") #this step will uodate result column
        ExcelUtils.fillGreenColor(file, "Sheet4", r, 8)
    else:
        print("test failed")
        ExcelUtils.writeData(file, "Sheet4", r, 8, "fail")
        ExcelUtils.fillRedColor(file, "Sheet4", r, 8)

    driverObj.find_element(By.XPATH, "//img[@class='PL5']").click() #click the clear for the next round of execution
    time.sleep(3)
driverObj.close()









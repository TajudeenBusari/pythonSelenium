from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
webdriver.Chrome()
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
webdriverObj.maximize_window()
min_slider=webdriverObj.find_element(By.XPATH, "XPATH OF THE MINIMUM SLIDER")
max_slider=webdriverObj.find_element(By.XPATH, "XPATH OF THE MAX SLIDER")
print(min_slider.location) ##gives some x,y coordinate in dictionary form {'x:'somevalue','y':'somevalue'}
print(max_slider.location) ##gives some x,y coordinate {'x:'somevalue','y':'somevalue'}
#in this case, only x axis can be moved cos it only in one dirction
#you can find location of any element



act=ActionChains(webdriverObj)
act.drag_and_drop_by_offset(min_slider, 200, 0).perform() #move x by 200 and leave y to 0
act.drag_and_drop_by_offset(max_slider, -35, 0).perform() #move x by -35 and leave y to 0

#if the slider is in vertical direction, work with y axix


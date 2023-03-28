from selenium import webdriver
from selenium.webdriver.common.by import By
import time
webdriverObj=webdriver.Chrome()
webdriverObj.get("https://money.rediff.com/gainers/bse/daily/groupa")
webdriverObj.maximize_window()
#SELF
'''Text_var=webdriverObj.find_element(By.XPATH, "//a[contains(text(), 'Indus Towers')]/self::a").text
print(Text_var)'''



#PARENT
'''Text_var=webdriverObj.find_element(By.XPATH, "//a[contains(text(), 'Indus Towers')]/parent::td").text
#td is the parent tag of self a from wehere we can also capture the text of the child
#if the parent tag #td has a value, it will be printed
print(Text_var)'''

#CHILD : FROM CHILD, WE CAPTURE THE ANCESTOR DATA which contains all child node values
#tr has so many child node td(with diffrent txts)
#we are not using txt method here cos we just want to get the total number of txt i.e length
#write a loop statement to get eah and every text
'''childs=webdriverObj.find_elements(By.XPATH, "//a[contains(text(), 'Indus Towers')]/ancestor::tr/child::td")
print(len(childs)) #out put 5'''

#ANCESTOR:
'''text_var=webdriverObj.find_element(By.XPATH, "//a[contains(text(), 'Indus Towers')]/ancestor::tr").text
#this will print the entire row of the ancestor tr

print(text_var) #output  A 159.30 168.05 + 5.49'''

#DESCENDANT:
'''descendants=webdriverObj.find_elements(By.XPATH, "//a[contains(text(), 'Indus Towers')]/ancestor::tr/descendant::*")
#this will return the descenndants of tr tag which are td
#the * will get all descendant since we assume we dont know

print("Number of descendants:", len(descendants)) #output 7'''


#FOLLOWING NODES:
'''following=webdriverObj.find_elements(By.XPATH, "//a[contains(text(), 'Indus Towers')]/ancestor::tr/following::*")
#this will return the follwing nodes
#the * will get all following  assume we dont know

print("Number of following is:", len(following))    #output :3127'''


#FOLLOWING-SIBLINGS:
'''followingSibling=webdriverObj.find_elements(By.XPATH, "//a[contains(text(), 'Indus Towers')]/ancestor::tr/following-sibling::*")

print("Number of following-sibling is:", len(followingSibling)) #output 373'''



#PRECEDING:
'''preceding=webdriverObj.find_elements(By.XPATH, "//a[contains(text(), 'Indus Towers')]/ancestor::tr/preceding::*")

print("Number of preceding is:", len(preceding)) #output  226

webdriverObj.close()'''

#PRECEDING-SIBLINGS:
precedingSiblings=webdriverObj.find_elements(By.XPATH, "//a[contains(text(), 'Indus Towers')]/ancestor::tr/preceding-sibling::tr")
#preceding sibling specifically for tr, you call do for all '*' as well
print("Number of preceding-sibling is:", len(precedingSiblings)) #output 9

webdriverObj.close()
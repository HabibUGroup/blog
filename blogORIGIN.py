#selenium install required
#pip install required
#pip install requests



from selenium import webdriver
from selenium.webdriver.common.keys import Keys   
#the above allows you to ender and whatnot
import time
from time import sleep
import random
import string
import requests



PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://habibugroup.github.io/blog/")
count = len(driver.find_elements_by_class_name('item-title'))
#print(count)



#driver.find_elements_by_class_name('classname')[1].click()
i = -1
while i < count - 1:
    i = i + 1
    #print(i)
    #print(count)
    linkone = driver.find_elements_by_class_name("item-title")[i]
    linkone.click()
    time.sleep(2)

    linkcheck = driver.current_url
    invalidlink = "https://habibugroup.github.io/blog/home/fsahja"
    r = requests.get(linkcheck)
    storedr = r.status_code
    if storedr == 200:
        print("Valid Page")
        print("---")
    if storedr == 404:
        print("1")
        print("404 Error")
        print("---")
   
    title = driver.find_element_by_class_name("title")
    print(title.text)

    time.sleep(2)
    driver.get("https://habibugroup.github.io/blog/")
    time.sleep(2)

    

time.sleep(2)
driver.close()




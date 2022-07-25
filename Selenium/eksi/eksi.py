from selenium import webdriver
import random
import time

#Creating Browser
browser = webdriver.Firefox()



#lesson 3
"""
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
entries = list()
pagCount = 1
total = 0

while pagCount < 11:
    randPage = random.randint(1,1290)
    newUrl = url + str(randPage)
    browser.get(newUrl)
    time.sleep(2)
    contents = browser.find_elements_by_css_selector(".content")
    for content in contents:
        entries.append(content.text)
    pagCount += 1
with open("text.txt","w",encoding="utf-8") as file:
    file.writelines(entries)    
"""
#Lesson 2
"""
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pagCount = 1
total = 0
while pagCount < 11:
    randPage = random.randint(1,1290)
    newUrl = url + str(randPage)
    browser.get(newUrl)
    time.sleep(2)
    contents = browser.find_elements_by_css_selector(".content")
    total += len(contents)
    for content in contents:
        print("***************************")
        print(content.text)
    pagCount += 1
print(total)
"""
#Lesson 1
"""
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712"

#Browser -> URL
browser.get(url)
time.sleep(3)

#browser -> URL classı content olanları al
contents = browser.find_elements_by_css_selector(".content")
for content in contents:
    print("****************************************")
    print(content.text)
"""     
browser.close()
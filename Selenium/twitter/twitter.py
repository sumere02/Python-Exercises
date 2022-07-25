from selenium import webdriver
import time


url = "https://twitter.com"
browser = webdriver.Firefox()
browser.get(url)
time.sleep(1)
login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div")
login.click()
time.sleep(10)
username = browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
next = browser.find_element_by_xpath("//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
username.send_keys("sumeremir@outlook.com")
n  ext.click()
time.sleep(10) 
browser.close()
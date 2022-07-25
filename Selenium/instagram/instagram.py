from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
url = "https://www.instagram.com/accounts/login/"
browser.get(url)
user = "emr_sumer"
pword = "exiled02"
wait = WebDriverWait(browser, 20)
wait.until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(user)
time.sleep(1)
wait.until(EC.element_to_be_clickable(( By.NAME, "password"))).send_keys(pword)
time.sleep(1)
wait.until(EC.element_to_be_clickable(( By.XPATH, "//*[@id='loginForm']/div/div[3]/button"))).click()
time.sleep(3)
wait.until(EC.element_to_be_clickable(( By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"._a9--._a9_1"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"emr_sumer"))).click()
time.sleep(5)
button = browser.find_elements_by_css_selector("._aa_5")
Button = button[1]
Button.click()
time.sleep(5)
jscommand = """
followers = document.querySelector("._aano");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage = followers.scrollHeight
return lenOfPage
"""
lenOfPage = browser.execute_script(jscommand)
match = False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(3)
followers = browser.find_elements_by_css_selector("._aacl._aaco._aacw._aacx._aad7._aade")
with open("instagram/followers.txt","w",encoding="utf-8") as file:
    for follower in followers:
        file.write(follower.text + "\n")
browser.close()



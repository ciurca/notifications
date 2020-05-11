from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\roman\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)

driver.get("https://facebook.com/")

#Facebook Notifications
try:
    fbnotif = driver.find_element_by_xpath('.//div[@class="uiToggle _4962 _4xi2 _z9r hasNew"]//span[@class="_51lp _3z_5 _5ugh"]')
    print("You have " + fbnotif.text + " new Facebook notifications.")
except NoSuchElementException:
    print("You have no new Facebook notifications.")

#Facebook Messenger notifications
try:
    fbms = driver.find_element_by_xpath('.//div[@class="uiToggle _4962 _1z4y _330i _4kgv hasNew"]//span[@class="_51lp _3z_5 _5ugh"]')
    print("You have " + fbms.text + " new Facebook messages.")
except NoSuchElementException:
    print("You have no new Facebook messages.")



driver.get("https://instagram.com/")

#Instagram messages
try:
    ignotif = driver.find_element_by_xpath('.//div[@class="bqXJH"]')
    print("You have " + ignotif.text + " new Instagram messages.")
except NoSuchElementException:
    print("You have no new Instagram messages.")



driver.get("https://twitter.com/home")
time.sleep(3)

#Twitter notifications
try:
    twnotif = driver.find_element_by_xpath('.//a[@href="/notifications"]//div[@class="css-901oao r-1awozwy r-urgr8i r-f6ebdl r-sdzlij r-1phboty r-rs99b7 r-1tjplnt r-jwli3a r-6koalj r-1q142lx r-1qd0xha r-1gkfh8e r-16dba41 r-50lct3 r-1777fci r-ad9z0x r-1b8eohn r-u8s1d r-kquydp r-1m4drjs r-3s2u2q r-qvutc0"]')
    print("You have " + twnotif.text + " new Twitter notifications.")
except NoSuchElementException:
    print("You have no new Twitter notifications.")

#Twitter DMs
try:
    twdm = driver.find_element_by_xpath('.//a[@href="/messages"]//div[@class="css-901oao r-1awozwy r-urgr8i r-f6ebdl r-sdzlij r-1phboty r-rs99b7 r-1tjplnt r-jwli3a r-6koalj r-1q142lx r-1qd0xha r-1gkfh8e r-16dba41 r-50lct3 r-1777fci r-ad9z0x r-1b8eohn r-u8s1d r-kquydp r-1m4drjs r-3s2u2q r-qvutc0"]')
    print("You have " + twdm.text + " new Twitter messages.")
except NoSuchElementException:
    print("You have no new Twitter messages.")


driver.quit()

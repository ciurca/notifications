from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\REPLACE\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)

def notifs(name, type, site, element, sleep):
    driver.get(site)
    time.sleep(sleep)

    try:
        elem = driver.find_element_by_xpath(element)
        print(f"You have {elem.text} new {name} {type}.")
    except NoSuchElementException:
        print(f"You have no new {name} {type}.")

notifs('Facebook', 'notification(s)', "https://facebook.com/", './/div[@class="uiToggle _4962 _4xi2 _z9r hasNew"]//span[@class="_51lp _3z_5 _5ugh"]', 0)
notifs('Facebook', 'message(s)', "https://facebook.com/", './/div[@class="uiToggle _4962 _1z4y _330i _4kgv hasNew"]//span[@class="_51lp _3z_5 _5ugh"]', 5)
notifs('Instagram', 'message(s)', "https://instagram.com/", './/div[@class="bqXJH"]', 0)
notifs('Twitter', 'notification(s)', "https://twitter.com/home", './/a[@href="/notifications"]//div[@class="css-901oao r-1awozwy r-urgr8i r-f6ebdl r-sdzlij r-1phboty r-rs99b7 r-1tjplnt r-jwli3a r-6koalj r-1q142lx r-1qd0xha r-1gkfh8e r-16dba41 r-50lct3 r-1777fci r-ad9z0x r-1b8eohn r-u8s1d r-kquydp r-1m4drjs r-3s2u2q r-qvutc0"]', 3)
notifs('Twitter', 'message(s)', "https://twitter.com/home", './/a[@href="/messages"]//div[@class="css-901oao r-1awozwy r-urgr8i r-f6ebdl r-sdzlij r-1phboty r-rs99b7 r-1tjplnt r-jwli3a r-6koalj r-1q142lx r-1qd0xha r-1gkfh8e r-16dba41 r-50lct3 r-1777fci r-ad9z0x r-1b8eohn r-u8s1d r-kquydp r-1m4drjs r-3s2u2q r-qvutc0"]', 3)

driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common import window
chrome_options=webdriver.ChromeOptions()#to initiate headless testing we need to call
chrome_options.add_argument("headless")#toinitiate headless testing( not invoking browser)
driver= webdriver.Chrome(options=chrome_options)
chrome_options.add_argument("__ignore-certificateerrors")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(2)
driver.get_screenshot_as_file("screen.png") #totakescreenshot
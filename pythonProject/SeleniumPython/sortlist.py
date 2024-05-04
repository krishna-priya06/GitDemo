import time

from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
# chrome_options=webdriver.ChromeOptions()#to initiate headless testing we need to call
# chrome_options.add_argument("headless")#toinitiate headless testing( not invoking browser)
# driver= webdriver.Chrome(options=chrome_options)
driver= webdriver.Chrome()
driver.implicitly_wait(2)
# chrome_options.add_argument("__ignore-certificateerrors")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
browsersortedlist=[]
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/div/div/header/div/div[3]/a[2]").click()
windowsopened=driver.window_handles
print(windowsopened)
driver.switch_to.window(windowsopened[1])
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
vegelem = driver.find_elements(By.XPATH,"//tr/td[1]")
for veggie in vegelem:
    browsersortedlist.append(veggie.text)
originalsortedlist=(browsersortedlist).copy()
browsersortedlist.sort()
print(originalsortedlist)
print(browsersortedlist)
assert browsersortedlist == originalsortedlist
# # //span[normalize-space()='Veg/fruit name']
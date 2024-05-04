import time

from selenium import webdriver
from selenium.webdriver.common.by import By
name= 'priya'
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,'name').send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
alerts=driver.switch_to.alert
altxt=alerts.text
print(altxt)
assert name in altxt
alerts.dismiss()
time.sleep(10)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
name= 'priya'
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
# altxt= alert.text
print(alert.text)
alert.accept()
time.sleep(10)

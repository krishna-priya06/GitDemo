import email
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"email").send_keys("krishnapriya.adavikolanu@gmail.com")








time.sleep(3)
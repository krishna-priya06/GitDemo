import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.set_window_size(1500, 1400)
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
time.sleep(5)
dropdown.select_by_visible_text("Male")
time.sleep(5)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
# driver.set_window_size(2000,2500)
driver.find_element(By.XPATH,"//a[@class='forgot-password-link']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter your email address']").send_keys('demo@gmail.com')
driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys('newpassword')
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys('newpassword')
driver.find_element(By.CLASS_NAME,"btn").click()









time.sleep(5)

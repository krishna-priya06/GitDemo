import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
openedwindows=driver.window_handles
driver.switch_to.window(openedwindows[1])
str=driver.find_element(By.XPATH,"//p[@class='im-para red']").text
print(str)
driver.switch_to.window(openedwindows[0])
totaltexts=str.split(" ")
print(totaltexts)
driver.find_element(By.ID,'username').send_keys(totaltexts[4])
driver.find_element(By.CSS_SELECTOR,'#password').send_keys('password')
driver.find_element(By.ID,"terms").click()
driver.find_element(By.NAME,'signin').click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
alert=driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text
print(alert)











time.sleep(5)
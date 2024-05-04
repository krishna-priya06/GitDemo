import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
print(count)
for result in results:
    result.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
driver.find_element(By.XPATH,"//button[@type='button']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebDriverWait(driver,20)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
discount=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(driver.find_element(By.CSS_SELECTOR,".discountPerc").text)
print(discount)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").click()
time.sleep(5)


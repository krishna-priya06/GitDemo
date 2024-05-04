import time

from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
mobiles = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
print(len(mobiles))
smartphones=[]
for mobile in mobiles:
    if  mobile.text.__contains__("Blackberry"):
        print (mobile.text)
        mobile.find_element(By.CSS_SELECTOR,".btn").click()
        driver.execute_script("window.scroll(0,200)")
driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("india")
wait=WebDriverWait(driver,20)
checkout=wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".suggestions")))
driver.find_element(By.CSS_SELECTOR,".suggestions").click()
time.sleep(2)
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)
# wait=WebDriverWait(driver,20)
alert=driver.find_element(By.CLASS_NAME,"alert").text
print(alert)

# suggestions = driver.find_element(By.CSS_SELECTOR,".suggestions")
# print(suggestions.text)
# suggestions.click()

# time.sleep(8)

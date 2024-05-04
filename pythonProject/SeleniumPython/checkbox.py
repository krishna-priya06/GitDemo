import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.NAME,'checkBoxOption2').click()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
len(checkboxes)
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=='option2':
        checkbox.click()







time.sleep(5)
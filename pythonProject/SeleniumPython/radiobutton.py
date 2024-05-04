import time

from selenium import webdriver
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobuttons))
for radiobutton in radiobuttons:
    if radiobutton.get_attribute('value')== 'radio1':
        radiobutton.click()
        assert radiobutton.is_selected()
        break
driver.execute_script("window.scrollBy(0,200)","")
driver.find_element(By.ID,'show-textbox').click()
time.sleep(5)
driver.find_element(By.ID,'hide-textbox').click()
assert not driver.find_element(By.CSS_SELECTOR,'#displayed-text').is_displayed()




time.sleep(10)
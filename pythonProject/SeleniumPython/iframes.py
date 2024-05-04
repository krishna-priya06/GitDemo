from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollTo(0,250)")
driver.switch_to.frame('iframe-name')
driver.find_element(By.XPATH,"//a[@href='practice-project']").click()
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("krishnapriya")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("krishnapriya.adavikolanu@gmail.com")
driver.find_element(By.CSS_SELECTOR,".agreeTerms").click()
# driver.find_element(By.CSS_SELECTOR,".form-submit").click()

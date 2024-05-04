from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(3)
driver.switch_to.frame(driver.find_element(By.ID,"mce_0_ifr"))
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate this frame")
driver.switch_to.default_content()#to switch back to the main html page from frame
print(driver.find_element(By.CSS_SELECTOR,"h3").text)

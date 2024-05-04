from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/windows")
# driver.find_element(By.XPATH,"//a[@href='/windows/new']").click()
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsopened=driver.window_handles
driver.switch_to.window(windowsopened[1])
print(windowsopened)
browser=driver.find_element(By.TAG_NAME,"h3").text
print(browser)
driver.close()
driver.switch_to.window(windowsopened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
driver.close()

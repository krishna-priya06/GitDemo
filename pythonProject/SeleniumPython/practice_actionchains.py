import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.find_element(By.XPATH,"/html/body/h1").text)

action=ActionChains(driver)
#action.context_click()-mouserightclick
#action.drag_and_drop()-dragdrop
# driver.execute_script("window.scrollTo(10,document.body.scrollHeight)")
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(5)
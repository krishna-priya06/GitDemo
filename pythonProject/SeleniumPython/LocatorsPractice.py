import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.set_window_size(1500, 1400)
driver.find_element(By.XPATH,"//input[@name ='name']").send_keys("krishnapriya adavikolanu")
driver.find_element(By.NAME,"email").send_keys("krishnapriya.adavikolau@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Hira@may2018")
driver.find_element(By.ID,"exampleCheck1").click()
checkbox=driver.find_element(By.ID,"exampleCheck1")
if checkbox.is_selected():
    driver.find_element(By.ID, "exampleCheck1").click()
dropdown= driver.find_element(By.ID,"exampleFormControlSelect1")
dropdown.send_keys("Female")
driver.find_element(By.ID,"inlineRadio2").click()
driver.find_element(By.NAME,"bday").send_keys("06/04/1993")
# bday=driver.find_element(By.NAME,"bday")
# print(bday.get_attribute('value'))
# assert (bday=='22/06/1993')
driver.find_element(By.XPATH,"//input[@type= 'submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
# driver.execute_script("window.scrollTo(0, 0);")
# driver.save_screenshot("success.png")
# driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()
# driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys('priya')
assert "success" in message
time.sleep(10)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj =Service()
driver= webdriver.Chrome(service= service_obj)
driver.get('https://linkedin.com')

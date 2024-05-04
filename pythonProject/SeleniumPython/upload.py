from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Excelupload:
    def test_modifyfruitprice(self):
        file_path="/Users/kiranpriya/Downloads/download.xlsx"
        driver=webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
        driver.find_element(By.ID,"downloadButton").click()
        uploadfile=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
        uploadfile.send_keys(file_path)
        wait=WebDriverWait(driver,5)
        toaster_element=(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
        wait.until(EC.visibility_of_element_located(toaster_element))
        print(driver.find_element(*toaster_element).text)


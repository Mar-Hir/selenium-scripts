# spisz sobie te gorne komendy
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DynamicControl:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/dynamic_controls"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        wait = WebDriverWait(driver, timeout=5)
        time.sleep(2)
        check = driver.find_element_by_xpath("//input[@type='checkbox']").click()
        time.sleep(2)
        rem = driver.find_element_by_xpath("//button[@type='button' and contains(text(),'Remove')]").click()
        wait.until(EC.presence_of_element_located((By.ID, "message")))

        butt = driver.find_element_by_xpath("//button[@type='button' and contains(text(),'Enable')]").click()
        wait.until(EC.presence_of_element_located((By.ID, "message")))

        field = driver.find_element_by_xpath("//input[@type='text']").send_keys("ulala")
        time.sleep(2)
        nbutt = driver.find_element_by_xpath("//button[@type='button' and contains(text(),'Disable')]").click()
        wait.until(EC.presence_of_element_located((By.ID, "message")))
        time.sleep(2)
        driver.quit()


ff = DynamicControl()
ff.test()





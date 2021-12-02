from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SwitchAd:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/entry_ad"
        driver = webdriver.Edge(executable_path="C:\\Users\\Marta\\drivers\\msedgedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        print(driver.title)
        wait = WebDriverWait(driver, timeout=5)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-title")))
        elcl = driver.find_element_by_xpath("//div[@class='modal-footer']/p")
        time.sleep(2)
        elcl.click()
        time.sleep(2)
        el = driver.find_element_by_xpath("//div[@class='example']/h3").text
        print(el)
        driver.quit()


ff = SwitchAd()
ff.test()
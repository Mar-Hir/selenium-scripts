from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Checkbox:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/checkboxes"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        el1 = driver.find_element_by_xpath("//input[@type='checkbox'][1]")
        el2 = driver.find_element_by_xpath("//input[@type='checkbox'][2]")
        el1.click()
        time.sleep(2)
        el2.click()
        time.sleep(2)


        driver.quit()


ff = Checkbox()
ff.test()

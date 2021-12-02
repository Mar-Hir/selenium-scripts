from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class DropDown:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/dropdown"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        element = driver.find_element_by_id("dropdown")
        sel = Select(element)
        sel.select_by_value("1")
        time.sleep(3)
        driver.quit()


ff = DropDown ()
ff.test()
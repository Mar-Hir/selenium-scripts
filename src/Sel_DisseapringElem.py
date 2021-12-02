from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Dissapearing:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/disappearing_elements"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get(baseUrl)
        try:
            el = driver.find_element_by_xpath("//a[contains(text(),'Gallery')]")
            print("I found it")
        except NoSuchElementException:
            print("Not found")
        driver.quit()


ff = Dissapearing()
ff.test()
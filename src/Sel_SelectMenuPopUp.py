from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class SelectedPopUP:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/context_menu"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        el1 = driver.find_element_by_xpath("//div[@id='hot-spot']")
        actions = ActionChains(driver)
        actions.context_click(el1).perform()
        time.sleep(3)
        alert1 = driver.switch_to.alert
        time.sleep(3)
        alert1.accept()
        time.sleep(3)
        driver.quit()


ff = SelectedPopUP()
ff.test()
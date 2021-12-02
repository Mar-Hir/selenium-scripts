from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Drag:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/drag_and_drop"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get(baseUrl)
        from_element = driver.find_element_by_xpath("//div[@id='column-b']")
        to_element = driver.find_element_by_xpath("//div[@id='column-a']")
        try:
            actions = ActionChains(driver)
            actions.click_and_hold(from_element).move_to_element(to_element).release().perform()
            # actions.drag_and_drop(from_element, to_element).perform()
            time.sleep(2)
        except:
            print("YOU FAIL")
        driver.quit()


ff = Drag()
ff.test()
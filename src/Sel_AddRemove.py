from selenium import webdriver
import time


class AddRemove:
    def test(self):
        baseUrl = "http://the-internet.herokuapp.com/add_remove_elements/"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        el1 = driver.find_element_by_xpath("//button[contains(text(),'Add Element')]")
        el1.click()
        el1.click()
        el1.click()
        time.sleep(3)
        el2 = driver.find_element_by_xpath("//div[@id='elements']//button[3]").click()
        time.sleep(2)

        driver.quit()


ff = AddRemove()
ff.test()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MoveView:
    def test(self):
        baseUrl = "https://www.cropp.com/pl/pl/zf754-01x/sweter-k-cropp"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        el = driver.find_element_by_xpath("//span[contains(text(),'Wybierz rozmiar')]")
        assert el.is_displayed()
        actions = ActionChains(driver)
        # actions.move_to_element_with_offset(el, -2000, -2000).perform()
        # actions.move_by_offset(-2000, -2000).perform()
        # actions.move_to_element(el).move_by_offset(400,400).perform()
        actions.move_to_element(el).click().perform()
        # actions.move_by_offset(600,-1).perform()
        # wait = WebDriverWait(driver, timeout=10)
        # wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-title']")))
        # elcl = driver.find_element_by_xpath("//div[@class='modal-footer']/p")
        time.sleep(4)




        driver.quit()


ff = MoveView()
ff.test()
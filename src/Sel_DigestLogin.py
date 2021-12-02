from selenium import webdriver
import time


class Login:
    def test(self):
        baseUrl = "http://admin:admin@the-internet.herokuapp.com/digest_auth"
        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        time.sleep(2)
        title = driver.title
        print(title)
        text = driver.find_element_by_xpath("//div[@class='example']//p").text
        print(text)
        driver.quit()


ff = Login()
ff.test()

#Test Scenario
# Read the details about the images present on the page. Send HTTP request for each image.
#Check the response code of the HTTP request. If the response code is 200, the image is not broken; else, the image is broken.
#Print whether the image is broken or not on the terminal.
# sprawdzam czy da sie pobrac obrazek, uzywajac url z atrybutu source, jezeli zawartosc jest dostepna to zwroci status kodu 200


from selenium import webdriver
import urllib3
import pytest
import requests
from requests.exceptions import InvalidURL, InvalidSchema, MissingSchema


class BrokenImg :
    def test(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        baseUrl = "http://the-internet.herokuapp.com/broken_images"

        driver = webdriver.Chrome(executable_path="C:\\Users\\Marta\\drivers\\chromedriver.exe")
        iBrokenImageCount = 0
        driver.maximize_window()
        driver.implicitly_wait(8)
        driver.get(baseUrl)
        image_list = driver.find_elements_by_tag_name("img")
        print('Total number of images on '+ baseUrl + ' are ' + str(len(image_list)))
        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code != 200:
                    print(img.get_attribute('outerHTML') + " is broken.")
                    iBrokenImageCount += 1

            except MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")


        driver.quit()

        print('The page ' + baseUrl + ' has ' + str(iBrokenImageCount) + ' broken images')


ff = BrokenImg()
ff.test()

# http://the-internet.herokuapp.com/broken_images/asdf.jpg
#
# http://the-internet.herokuapp.com/img/avatar-blank.jpg
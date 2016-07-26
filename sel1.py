from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.get('https://www.facebook.com')

    def test_Login(self):
        driver = self.driver
        facebookUsername    = "dagmar.mocarnikova@gmail.com"
        facebookPassword    = ""
        emailFieldID        = "email"
        passFieldID         = "pass"
        loginButtonXpath    = "//input[@value ='Log In']"
        fbLogoXpath         = "(//a[contains(@href, 'logo')])[1]"

        emailFieldElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonElement))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)

        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)

        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: find_element_by_xpath(fbLogoXpath))



    def tearDown(self):
        self.driver.quit()

if __name__ == "__name__":
    unittest.main()

"""""


driver.implicitly_wait(20)
driver.find_element_by_id("email").send_keys("Selenium Webdriver")
driver.find_element_by_name("pass").send_keys("Python")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("Facebook.png")
driver.quit()"""
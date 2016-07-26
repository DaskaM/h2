from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import unittest

class AweberTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')

    def test_title(self):

        self.driver.get("https://en.wikipedia.org/wiki/Software_testing")
        title_el = self.driver.find_element_by_id("firstHeading")
        self.assertEqual(title_el.text, 'Software testing')

    def test_search(self):
        self.driver.get("https://en.wikipedia.org/wiki/Software_testing")
        self.driver.find_element_by_id("searchInput").send_keys('slovak')


    def test_select(self):
         self.driver.get("https://en.wikipedia.org/wiki/Software_testing")
         select = self.driver.find_elements_by_class_name("toctext")

         for option in select:
            if option.text == "Economics":
                option.click()

    def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        search_window = find_element_by_id("simpleSearch")
        search_window.send_keys("slovak")
        search_window.click()
        search_window.send_keys(Keys.RETURN)


	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()

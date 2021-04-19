import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

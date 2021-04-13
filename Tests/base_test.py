import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)

    def tearDown(self):
        self.driver.quit()

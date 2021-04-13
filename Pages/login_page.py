from Pages.base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    def insert_username(self, username):
        element = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
        element.send_keys(username)

    def insert_password(self, password):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        element.send_keys(password)

    def check_error_visible(self):
        element = self.driver.find_element(*LoginPageLocators.ERROR_LOGIN)
        element.is_displayed()

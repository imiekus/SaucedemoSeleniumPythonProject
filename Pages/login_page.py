from Pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):

    def insert_username(self, username):
        element = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
        element.send_keys(username)

    def insert_password(self, password):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        element.send_keys(password)

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        element.click()

    def successful_login(self, username, password):
        self.insert_username(username)
        self.insert_password(password)
        self.click_login_button()

    def check_error_visible(self):
        element = self.driver.find_element(*LoginPageLocators.ERROR_LOGIN)
        element.is_displayed()

    def check_login_button_exists(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        element.is_displayed()

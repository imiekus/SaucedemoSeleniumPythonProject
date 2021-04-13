from Pages.base_page import BasePage
from locators import InventoryPageLocators
import time


class InventoryPage(BasePage):

    def check_logout_exists(self):
        element = self.driver.find_element(*InventoryPageLocators.LOGOUT_BUTTON)
        element.is_displayed()

    def logout_user(self):
        element1 = self.driver.find_element(*InventoryPageLocators.MENU_BUTTON)
        element2 = self.driver.find_element(*InventoryPageLocators.LOGOUT_BUTTON)
        element1.click()
        element2.click()

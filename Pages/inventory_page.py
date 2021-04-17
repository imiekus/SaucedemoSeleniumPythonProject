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

    def click_cart_button(self):
        element = self.driver.find_element(*InventoryPageLocators.SHOPPING_CART)
        element.click()

    def check_cart_badge_is_one(self):
        element = self.driver.find_element(*InventoryPageLocators.CART_BADGE)
        assert element.text == '1'

    def check_cart_badge_is_none(self):
        try:
            element = self.driver.find_element(*InventoryPageLocators.CART_BADGE)
            if element.is_displayed():
                raise Exception("Element should not be found")
        except:
            pass

    def check_if_backpack_button_status_is_add(self):
        element = self.driver.find_element(*InventoryPageLocators.ADD_TO_CART_BACKPACK)
        element.is_displayed()

    def check_if_button_status_is_remove(self):
        element = self.driver.find_element(*InventoryPageLocators.REMOVE_FROM_CART_BACKPACK)
        element.is_displayed()

    def add_backpack_to_cart(self):
        element = self.driver.find_element(*InventoryPageLocators.ADD_TO_CART_BACKPACK)
        element.click()

    def remove_backpack_from_cart(self):
        element = self.driver.find_element(*InventoryPageLocators.REMOVE_FROM_CART_BACKPACK)
        element.click()


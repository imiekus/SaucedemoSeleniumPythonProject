from Pages.base_page import BasePage
from locators import CartPageLocators


class CartPage(BasePage):

    def check_if_cart_is_empty(self):
        try:
            element = self.driver.find_element(*CartPageLocators.CART_ITEM)
            if element.is_displayed():
                raise Exception("Element should not be found")
        except:
            pass

from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.cart_page import CartPage
from TestData.test_data_setup import TestData


class CartPageTest(BaseTest):

    def setUp(self):
        super().setUp()
        lp = LoginPage(self.driver)
        lp.successful_login(username=TestData.USERNAME, password=TestData.PASSWORD)

    def test_cart_is_empty(self):
        print('Cart Page Test TC_1: Check if shopping cart is empty')
        self.driver.implicitly_wait(5)
        ip = InventoryPage(self.driver)
        cp = CartPage(self.driver)
        ip.click_cart_button()
        cp.check_if_cart_is_empty()


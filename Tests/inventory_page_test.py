from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage


class InventoryPageTest(BaseTest):

    def setUp(self):
        super().setUp()
        lp = LoginPage(self.driver)
        lp.successful_login(username='standard_user', password='secret_sauce')

    def test_logout(self):
        print('Inventory Page Test TC_1: Logout from service')
        self.driver.implicitly_wait(5)
        lp = LoginPage(self.driver)
        ip = InventoryPage(self.driver)
        ip.logout_user()
        lp.check_login_button_exists()

    def test_add_and_remove_backpack(self):
        print('Inventory Page Test TC_2: Check if user can add and remove element from cart at inventory page')
        ip = InventoryPage(self.driver)
        self.driver.implicitly_wait(5)
        ip.check_if_backpack_button_status_is_add()
        ip.add_backpack_to_cart()
        ip.check_if_button_status_is_remove()
        ip.check_cart_badge_is_one()
        ip.remove_backpack_from_cart()
        ip.check_if_backpack_button_status_is_add()
        ip.check_cart_badge_is_none()


from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from ddt import ddt, data, unpack
from get_data import get_csv_data
import time


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

from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from ddt import ddt, data, unpack
from TestData.get_data import get_csv_data


@ddt
class LoginTest(BaseTest):

    def setUp(self):
        super().setUp()

    @data(*get_csv_data('/home/tester/PycharmProjects/seleniumWebProject/TestData/locked_out_user.csv'))
    @unpack
    def test_login_error(self, username, password):
        print('Login Page Test TC_1: Try to log in using locked out user credentials and check if error appears')
        lp = LoginPage(self.driver)
        lp.insert_username(username)
        lp.insert_password(password)
        lp.click_login_button()
        lp.check_error_visible()

    @data(*get_csv_data('/home/tester/PycharmProjects/seleniumWebProject/TestData/standard_user.csv'))
    @unpack
    def test_login_success(self, username, password):
        print('Login Page Test TC_2: Login with valid credentials and check if logged by searching for logout button')
        lp = LoginPage(self.driver)
        ip = InventoryPage(self.driver)
        lp.insert_username(username)
        lp.insert_password(password)
        lp.click_login_button()
        ip.check_logout_exists()




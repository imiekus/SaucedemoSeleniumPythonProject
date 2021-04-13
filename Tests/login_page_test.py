import unittest
from Tests.base_test import BaseTest
from Pages.login_page import LoginPage
from ddt import ddt, data, unpack
from get_data import get_csv_data


@ddt
class LoginTest(BaseTest):

    def setUp(self):
        super().setUp()

    @data(*get_csv_data('../TestData/locked_out_user.csv'))
    @unpack
    def test_login_error(self, username, password):
        print('TC_1: Try to log in using locked out user credentials')
        lp = LoginPage
        lp.insert_username(username)
        lp.insert_password(password)
        lp.check_error_visible()




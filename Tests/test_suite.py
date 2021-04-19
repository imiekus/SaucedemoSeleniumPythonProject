import unittest
from Tests.login_page_test import LoginTest
from Tests.inventory_page_test import InventoryPageTest
from Tests.cart_page_test import CartPageTest

tst1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tst2 = unittest.TestLoader().loadTestsFromTestCase(InventoryPageTest)
tst3 = unittest.TestLoader().loadTestsFromTestCase(CartPageTest)


test_suite = unittest.TestSuite([tst1, tst2, tst3])
unittest.TextTestRunner(verbosity=1).run(test_suite)

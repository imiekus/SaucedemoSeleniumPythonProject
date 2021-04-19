# SaucedemoSeleniumPythonProject
This project is my first project using Selenium with Python. 

## Prequisities
1. Python3 is installed and added to the PATH;
2. Selenium is installed;
3. Downloaded and installed python ddt module;

## Steps:
1. Clone the repository;
2. To run all tests please execute 'Tests/test_suite.py' file; to run tests separately, please execute chosen file;

## Test cases that were automated

#### Login Page Test TC_1: Try to log in using locked out user credentials and check if error appears
1. Insert locked out username.
2. Insert password.
3. Click on login button.
4. Check if error is visible.

#### Login Page Test TC_2: Login with valid credentials and check if logged by searching for logout button
1. Insert username.
2. Insert password.
3. Click on login button.
4. Check if logout button exists.

#### Inventory Page Test TC_1: Logout from service
1. Click on logout button.
2. Check if login button exists.

#### Inventory Page Test TC_2: Check if user can add and remove element from cart at inventory page
1. Check if backpack item button status is "add".
2. Add backpack to cart.
3. Check if backpack item button status is "remove".
4. Check if cart badge number "1".
5. Remove backpack from cart.
6. Check if backpack item button status is "add".
7. Check if cart badge number is none.

#### Cart Page Test TC_1: Check if shopping cart is empty
1. Click on cart button.
2. Check if shopping cart is empty.

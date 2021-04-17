from selenium.webdriver.common.by import By


class LoginPageLocators():
    USERNAME_INPUT = (By.XPATH, '//input[@data-test="username"]')
    PASSWORD_INPUT= (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BTN = (By.XPATH, '//input[@data-test="login-button"]')
    ERROR_LOGIN = (By.XPATH, '//h3[@data-test="error"]')


class InventoryPageLocators():
    MENU_BUTTON = (By.CLASS_NAME, 'bm-burger-button')
    LOGOUT_BUTTON = (By.ID, 'logout_sidebar_link')
    SHOPPING_CART = (By.ID, 'shopping_cart_container')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    ADD_TO_CART_BACKPACK = (By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    REMOVE_FROM_CART_BACKPACK = (By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')


class CartPageLocators():
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
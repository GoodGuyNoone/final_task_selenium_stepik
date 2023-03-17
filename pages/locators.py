from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_NAME_IN_NOTIFICATION = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    PRODUCT_PRICE_IN_NOTIFICATION = (By.CSS_SELECTOR, ".alertinner > p > strong")


from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_on_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # verify that login page is opened and contain "login" in url
        assert "login" in self.browser.current_url, "'Login' is not presented in url"

    def should_be_login_form(self):
        # verify that login form is presented on page
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "'Login form' is not presented on page"

    def should_be_register_form(self):
        # verify that registration form is presented on page
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM), "'Registration form' is not presented on page"

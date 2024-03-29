import math

from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # open given link
        self.browser.get(self.url)

    def go_to_login_page(self):
        # open login page
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):
        # open basket
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_login_link(self):
        # verify that page have login link
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        # find if element is presented on page
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def solve_quiz_and_get_code(self):
        # function to solve puzzle when it appeared on the page
        # given by dev team
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        # verify that user was authorized
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def is_not_element_present(self, how, what, timeout=4):
        # verify that element is not presented on the page
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        # verify that item on the page is disappeared
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def product_price_equal_price_in_notification(self):
        # verify that price in product page is equal to price in notification
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_NOTIFICATION).text, \
               "Product price is not equal to price in notification"

    def product_name_equal_name_in_notification(self):
        # verify that name in product page is equal to name in notification
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_NOTIFICATION).text, \
               f"Product name is not equal to name in notification."

    def should_not_be_success_message(self):
        # verify that success message is not presented on page
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        # verify that success message is disappeared
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

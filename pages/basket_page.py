from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        # verify that basket have no items in it
        assert self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS) == [], "Basket is not empty, but should be"

    def should_be_your_basket_is_empty_text(self):
        # verify that page "your basket is empty" text
        your_basket_is_empty = self.browser.find_element(*BasketPageLocators.NO_ITEM_TEXT).text.strip()
        print(your_basket_is_empty)
        assert "Your basket is empty." in your_basket_is_empty, \
               "'Your basket is empty' text is not presented"

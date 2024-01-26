from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Информация о пустой корзине отсутствует"
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "empty" in empty_basket_text

    def should_be_no_items_in_basket(self):
        basket_items = self.browser.find_elements(*BasketPageLocators.BASKET_ITEMS)
        assert len(basket_items) == 0
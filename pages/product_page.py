from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Наименование товара отсуствует"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Стоимость товара отсуствует"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_name_in_notification(self):
        self.product_name_in_notification = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_NOTIFICATION).text
        assert self.product_name == self.product_name_in_notification, "Наименования товаров не совпадают"

    def should_be_product_price_in_notification(self):
        self.product_price_in_notification = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_NOTIFICATION).text
        assert self.product_price == self.product_price_in_notification, "Стоимость товара и цена корзины не совпадают"  

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение об успешном добавлении в корзину присутствует, но не должно"

    def should_element_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Элемент не пропадает"

    



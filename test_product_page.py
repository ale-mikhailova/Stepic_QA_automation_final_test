import time
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By

def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open_browser()
    page.should_be_product_name()
    page.should_be_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_product_name_in_notification()
    page.should_be_product_price_in_notification()


import pytest
import time
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("promo", [*range (1,7), pytest.param(7, marks=pytest.mark.xfail), *range (8,10)])
def test_guest_can_add_product_to_basket(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}"
    page = ProductPage(browser, link)
    page.open_browser()
    page.should_be_product_name()
    page.should_be_product_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_product_name_in_notification()
    page.should_be_product_price_in_notification()


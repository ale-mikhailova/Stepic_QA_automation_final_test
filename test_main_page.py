import time
import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from selenium.webdriver.common.by import By


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open_browser()
        page.should_be_login_link()

    def test_guest_can_go_to_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open_browser()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.go_to_basket
class TestBasketMainPAge():
    def test_guest_can_see_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open_browser()
        page.should_see_basket_button()

    def test_quest_can_go_to_basket_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open_browser()
        page.go_to_basket_page()

    def test_empty_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open_browser()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_no_items_in_basket()
        basket_page.should_be_empty_basket_text()
       



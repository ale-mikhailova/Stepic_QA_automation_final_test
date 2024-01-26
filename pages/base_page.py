from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
from .locators import BasketPageLocators
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open_browser(self):
        self.browser.get(self.url)


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Кнопка логин отсутствует"
    

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
    

    def should_go_to_basket_button(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BUTTON), "Кнопка Перейти в корзину отсутствует"


    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        login_link.click()


    def is_element_present(self, method, css_selector):
        try:
            self.browser.find_element(method, css_selector)
        except (NoSuchElementException):
            return False
        return True


    def is_not_element_present(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return True
        return False


    def is_disappeared(self, method, css_selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return False
        return True


    def solve_quiz_and_get_code(self, timeout=4):
        WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("No second alert present")
        
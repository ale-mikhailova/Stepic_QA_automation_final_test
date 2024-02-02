import time
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegisterPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Incorrect login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self):
        email_field = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        email = str(time.time())+"@fakemail.org"
        email_field.send_keys(email)
        password_field = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        password = str(time.time())
        password_field.send_keys(password)
        password2_field = self.browser.find_element(*RegisterPageLocators.REGISTER_CONFIRM_PASSWORD)
        password2_field.send_keys(password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()



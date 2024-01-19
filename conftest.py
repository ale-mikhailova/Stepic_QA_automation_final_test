import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="Choose language: en-gb, ru, de, fr or etc")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(options=options)

    yield browser
    browser.quit()
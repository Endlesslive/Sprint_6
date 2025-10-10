# conftest.py или tests/conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


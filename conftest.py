import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации и завершения работы браузера"""
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    """Фикстура для инициализации главной страницы"""
    from pages.main_page import MainPage
    driver.get("https://qa-scooter.praktikum-services.ru/")
    return MainPage(driver)

@pytest.fixture(scope="function")
def faq_page(driver):
    """Фикстура для инициализации страницы FAQ"""
    from pages.faq_page import FAQPage
    driver.get("https://qa-scooter.praktikum-services.ru/")
    return FAQPage(driver)

@pytest.fixture(scope="function")
def order_page(driver):
    """Фикстура для инициализации страницы заказа"""
    from pages.order_page import OrderPage
    return OrderPage(driver)
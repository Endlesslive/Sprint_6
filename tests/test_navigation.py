import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class TestNavigation:
    """Тесты для проверки навигации по логотипам"""
    
    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и завершения работы браузера"""
        firefox_driver = webdriver.Firefox()
        firefox_driver.maximize_window()
        yield firefox_driver
        firefox_driver.quit()
    
    @allure.feature("Навигация")
    @allure.story("Клик по логотипу Самоката")
    @allure.title("Проверка перехода на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_returns_to_main_page(self, driver):
        """Проверка: клик по логотипу Самоката возвращает на главную страницу"""
        with allure.step("Открываем главную страницу"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
        
        with allure.step("Переходим на страницу заказа"):
            main_page = MainPage(driver)
            main_page.click_order_button_top()
        
        with allure.step("Кликаем по логотипу Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверяем, что вернулись на главную страницу"):
            current_url = driver.current_url
            assert "qa-scooter.praktikum-services.ru" in current_url
            assert "order" not in current_url
    
    @allure.feature("Навигация")
    @allure.story("Клик по логотипу Яндекса")
    @allure.title("Проверка открытия Дзена в новом окне при клике на логотип Яндекса")
    def test_yandex_logo_opens_dzen_in_new_window(self, driver):
        """Проверка: клик по логотипу Яндекса открывает Дзен в новом окне"""
        with allure.step("Открываем главную страницу"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
        
        with allure.step("Сохраняем текущее окно"):
            original_window = driver.current_window_handle
        
        with allure.step("Кликаем по логотипу Яндекса"):
            main_page = MainPage(driver)
            main_page.click_yandex_logo()
        
        with allure.step("Ожидаем открытия нового окна"):
            wait = WebDriverWait(driver, 10)
            wait.until(EC.number_of_windows_to_be(2))
            all_windows = driver.window_handles
        
        with allure.step("Переключаемся на новое окно"):
            for window in all_windows:
                if window != original_window:
                    driver.switch_to.window(window)
                    break
        
        with allure.step("Ожидаем загрузки страницы и проверяем URL"):
            # Ждём, пока URL изменится с about:blank
            wait.until(lambda d: d.current_url != "about:blank")
            # Даём время на редирект
            wait.until(lambda d: "dzen.ru" in d.current_url or "yandex" in d.current_url)
            current_url = driver.current_url
            assert "dzen.ru" in current_url or "yandex" in current_url, \
                f"Ожидался переход на Дзен, но открылся URL: {current_url}"

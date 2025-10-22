import pytest
import allure

class TestNavigation:
    @allure.feature("Навигация")
    @allure.story("Клик по логотипу Самоката")
    @allure.title("Проверка перехода на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_returns_to_main_page(self, main_page):
        with allure.step("Переходим на страницу заказа"):
            main_page.click_order_button_top()
        with allure.step("Кликаем по логотипу Самоката"):
            main_page.click_scooter_logo()
        with allure.step("Проверяем, что вернулись на главную страницу"):
            assert main_page.is_on_main_page(), \
                f"Не вернулись на главную страницу. Текущий URL: {main_page.get_current_url()}"

    @allure.feature("Навигация")
    @allure.story("Клик по логотипу Яндекса")
    @allure.title("Проверка открытия Дзена в новом окне при клике на логотип Яндекса")
    def test_yandex_logo_opens_dzen_in_new_window(self, main_page):
        """Проверка: клик по логотипу Яндекса открывает Дзен в новом окне"""
        with allure.step("Кликаем по логотипу Яндекса и переключаемся на новое окно"):
            main_page.open_yandex_logo_in_new_window()
        with allure.step("Проверяем, что открылась страница Яндекса/Дзена"):
            current_url = main_page.get_current_url()
            assert "dzen.ru" in current_url or "yandex" in current_url, \
                f"Ожидался переход на Дзен или Яндекс, но открылся URL: {current_url}"

import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrderFlowFromTop:
    @pytest.mark.parametrize("user_data", [
        {
            "name": "Иван",
            "surname": "Иванов",
            "address": "Москва, Ленина, 1",
            "metro": "Сокольники",
            "phone": "+79991234567",
            "date": "15.11.2025",
            "rental_period": "сутки",
            "color": "чёрный"
        },
        {
            "name": "Мария",
            "surname": "Петрова",
            "address": "СПб, Невский, 10",
            "metro": "Красносельская",
            "phone": "+79997654321",
            "date": "20.11.2025",
            "rental_period": "двое суток",
            "color": "серый"
        }
    ])
    @allure.feature("Функциональность заказа")
    @allure.story("Создание заказа через верхнюю кнопку")
    @allure.title("Проверка создания заказа через верхнюю кнопку 'Заказать'")
    @allure.description("Тест проверяет полный флоу создания заказа через верхнюю кнопку с разными данными")
    def test_order_creation_from_top_button(self, driver, user_data):
        """Проверка позитивного сценария создания заказа через верхнюю кнопку"""
        with allure.step("Открываем главную страницу"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
            main_page = MainPage(driver)
        with allure.step("Нажимаем верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        with allure.step("Заполняем форму с личными данными"):
            order_page = OrderPage(driver)
            order_page.fill_personal_info(user_data)
        with allure.step("Заполняем форму с параметрами аренды"):
            order_page.fill_rental_info(user_data)
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
        with allure.step("Проверяем, что сообщение об успехе отображается"):
            assert order_page.is_success_message_displayed(), \
                "Сообщение об успешном создании заказа не отображается"
        with allure.step("Проверяем текст сообщения об успехе"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Ожидалось сообщение 'Заказ оформлен', получено: {success_message}"

class TestOrderFlowFromBottom:
    @pytest.mark.parametrize("user_data", [
        {
            "name": "Иван",
            "surname": "Иванов",
            "address": "Москва, Ленина, 1",
            "metro": "Сокольники",
            "phone": "+79991234567",
            "date": "15.11.2025",
            "rental_period": "сутки",
            "color": "чёрный"
        },
        {
            "name": "Мария",
            "surname": "Петрова",
            "address": "СПб, Невский, 10",
            "metro": "Красносельская",
            "phone": "+79997654321",
            "date": "20.11.2025",
            "rental_period": "двое суток",
            "color": "серый"
        }
    ])
    @allure.feature("Функциональность заказа")
    @allure.story("Создание заказа через нижнюю кнопку")
    @allure.title("Проверка создания заказа через нижнюю кнопку 'Заказать'")
    @allure.description("Тест проверяет полный флоу создания заказа через нижнюю кнопку с разными данными")
    def test_order_creation_from_bottom_button(self, driver, user_data):
        """Проверка позитивного сценария создания заказа через нижнюю кнопку"""
        with allure.step("Открываем главную страницу"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
            main_page = MainPage(driver)
        with allure.step("Нажимаем нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        with allure.step("Заполняем форму с личными данными"):
            order_page = OrderPage(driver)
            order_page.fill_personal_info(user_data)
        with allure.step("Заполняем форму с параметрами аренды"):
            order_page.fill_rental_info(user_data)
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
        with allure.step("Проверяем, что сообщение об успехе отображается"):
            assert order_page.is_success_message_displayed(), \
                "Сообщение об успешном создании заказа не отображается"
        with allure.step("Проверяем текст сообщения об успехе"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message, \
                f"Ожидалось сообщение 'Заказ оформлен', получено: {success_message}"

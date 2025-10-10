import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderFlow:
    """Тесты для проверки процесса заказа"""
    
    @pytest.mark.parametrize("entry_point,user_data", [
    ("top", {
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, Ленина, 1",
        "metro": "Сокольники",
        "phone": "+79991234567",
        "date": "15.11.2025",
        "rental_period": "сутки",
        "color": "чёрный"
    }),
    ("bottom", {
        "name": "Мария",
        "surname": "Петрова",
        "address": "СПб, Невский, 10",
        "metro": "Красносельская",
        "phone": "+79997654321",
        "date": "20.11.2025",
        "rental_period": "двое суток",
        "color": "серый"
    })
])

    @allure.feature("Функциональность заказа")
    @allure.story("Создание заказа")
    @allure.title("Проверка позитивного сценария заказа через точку входа: {entry_point}")
    @allure.description("Тест проверяет полный флоу создания заказа с разными данными")
    def test_order_creation_flow(self, driver, entry_point, user_data):
        """Проверка позитивного сценария создания заказа"""
        with allure.step("Открываем главную страницу"):
            driver.get("https://qa-scooter.praktikum-services.ru/")
        
        with allure.step(f"Нажимаем кнопку Заказать ({entry_point})"):
            main_page = MainPage(driver)
            if entry_point == "top":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()
        
        with allure.step("Заполняем форму с личными данными"):
            order_page = OrderPage(driver)
            order_page.fill_personal_info(user_data)
        
        with allure.step("Заполняем форму с параметрами аренды"):
            order_page.fill_rental_info(user_data)
        
        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
        
        with allure.step("Проверяем успешное создание заказа"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message

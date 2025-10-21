from pages.base_page import BasePage
from locators.page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_order_button_top(self):
        """Клик по кнопке Заказать вверху страницы"""
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        """Клик по кнопке Заказать внизу страницы"""
        self.scroll_to_bottom()
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    def is_on_main_page(self):
        """Проверка, что находимся на главной странице"""
        current_url = self.get_current_url()
        return "qa-scooter.praktikum-services.ru" in current_url and "order" not in current_url
    
    def open_yandex_logo_in_new_window(self):
        """Открытие Яндекса в новом окне через логотип"""
        original_window = self.get_window_handle()
        self.click_yandex_logo()
        self.wait_for_new_window(2)
        self.switch_to_new_window(original_window)
        self.wait_for_url_change()
    
    def verify_yandex_page_opened(self):
        """Проверка, что открылась страница Яндекса/Дзена"""
        if self.wait_for_url_contains("dzen.ru", timeout=10):
            return True
        if self.wait_for_url_contains("yandex", timeout=10):
            return True
        return False

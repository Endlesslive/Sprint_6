from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы"""
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы"""
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

class OrderPageLocators:
    """Локаторы для страницы оформления заказа"""
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN = (By.XPATH, "//div[contains(@class, 'select-search__select')]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.XPATH, "//div[contains(@class, 'react-datepicker__month')]")
    RENTAL_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') or contains(text(), 'Заказ оформлен')]")

class FAQPageLocators:
    """Локаторы для страницы с вопросами"""
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FourPart')]")
    FAQ_TITLE = (By.XPATH, "//div[contains(@class, 'Home_SubHeader')]")
    
    @staticmethod
    def get_faq_question_locator(index):
        """Возвращает локатор для вопроса по индексу"""
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def get_faq_answer_locator(index):
        """Возвращает локатор для ответа по индексу"""
        return (By.ID, f"accordion__panel-{index}")

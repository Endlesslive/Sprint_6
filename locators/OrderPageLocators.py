from selenium.webdriver.common.by import By

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

    COLOR_CHECKBOXES = {
        'чёрный': BLACK_CHECKBOX,
        'серый': GREY_CHECKBOX,
        'black': BLACK_CHECKBOX,
        'grey': GREY_CHECKBOX
    }
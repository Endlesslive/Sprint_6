from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_personal_info(self, user_data):
        # Имя
        name_input = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.NAME_INPUT)
        )
        name_input.send_keys(user_data['name'])
        # Фамилия
        surname_input = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.SURNAME_INPUT)
        )
        surname_input.send_keys(user_data['surname'])
        # Адрес
        address_input = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.ADDRESS_INPUT)
        )
        address_input.send_keys(user_data['address'])
        # Метро
        metro_input = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_INPUT)
        )
        metro_input.click()
        metro_input.send_keys(user_data['metro'])
        # Ждём появления выпадающего списка и выбираем
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.METRO_DROPDOWN)
        )
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        # Телефон
        phone_input = self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.PHONE_INPUT)
        )
        phone_input.send_keys(user_data['phone'])
        # Кнопка Далее
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    def fill_rental_info(self, user_data):
        # Дата доставки
        date_input = self.wait.until(
            EC.element_to_be_clickable(OrderPageLocators.DATE_INPUT)
        )
        date_input.send_keys(user_data['date'])
        date_input.send_keys(Keys.ENTER)
        # Ждём закрытия календаря
        self.wait.until(
            EC.invisibility_of_element_located(OrderPageLocators.CALENDAR)
        )
        # Срок аренды
        self.click_element(OrderPageLocators.RENTAL_DROPDOWN)
        # Ждём появления опций
        self.wait.until(
            EC.presence_of_element_located(OrderPageLocators.RENTAL_OPTION)
        )
        # Выбираем нужный период
        from selenium.webdriver.common.by import By
        rental_option_locator = (
            By.XPATH, 
            f"//div[contains(@class, 'Dropdown-option') and text()='{user_data['rental_period']}']"
        )
        self.click_element(rental_option_locator)
        # Цвет самоката
        if user_data['color'] == 'чёрный':
            self.click_element(OrderPageLocators.BLACK_CHECKBOX)
        elif user_data['color'] == 'серый':
            self.click_element(OrderPageLocators.GREY_CHECKBOX)
    
    def confirm_order(self):
        order_buttons = self.find_elements(OrderPageLocators.ORDER_BUTTON)
        order_button = order_buttons[-1]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        self.wait.until(lambda d: order_button.is_displayed())
        order_button.click()
        self.click_element(OrderPageLocators.YES_BUTTON)
    
    def get_success_message(self):
        return self.get_element_text(OrderPageLocators.SUCCESS_MESSAGE)
    
    def is_success_message_displayed(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE)

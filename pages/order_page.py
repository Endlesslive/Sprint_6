from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class OrderPage:
    """Page Object для страницы оформления заказа"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def fill_personal_info(self, user_data):
        """Заполнение первой формы с личными данными"""
        # Имя
        name_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='* Имя']"))
        )
        name_input.send_keys(user_data['name'])
        
        # Фамилия
        surname_input = self.driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']")
        surname_input.send_keys(user_data['surname'])
        
        # Адрес
        address_input = self.driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        address_input.send_keys(user_data['address'])
        
        # Метро
        metro_input = self.driver.find_element(By.XPATH, "//input[@placeholder='* Станция метро']")
        metro_input.click()
        metro_input.send_keys(user_data['metro'])
        time.sleep(1)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)
        
        # Телефон
        phone_input = self.driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        phone_input.send_keys(user_data['phone'])
        
        # Кнопка Далее
        next_button = self.driver.find_element(By.XPATH, "//button[text()='Далее']")
        next_button.click()
    
    def fill_rental_info(self, user_data):
        """Заполнение второй формы с параметрами аренды"""
        time.sleep(2)  # Ждём загрузки второй формы
        
        # Дата доставки
        date_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='* Когда привезти самокат']"))
        )
        date_input.send_keys(user_data['date'])
        date_input.send_keys(Keys.ENTER)
        time.sleep(1)
        
        # Срок аренды
        rental_dropdown = self.driver.find_element(By.CLASS_NAME, "Dropdown-placeholder")
        rental_dropdown.click()
        time.sleep(0.5)
        
        # Выбираем нужный период
        rental_option = self.driver.find_element(
            By.XPATH, f"//div[@class='Dropdown-option' and text()='{user_data['rental_period']}']"
        )
        rental_option.click()
        
        # Цвет самоката
        if user_data['color'] == 'чёрный':
            black_checkbox = self.driver.find_element(By.ID, "black")
            black_checkbox.click()
        elif user_data['color'] == 'серый':
            grey_checkbox = self.driver.find_element(By.ID, "grey")
            grey_checkbox.click()
    
    def confirm_order(self):
        """Подтверждение заказа"""
        # Кнопка "Заказать" в нижней части формы
        order_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Заказать')]")
        # Берём последнюю кнопку (на форме заказа)
        order_button = order_buttons[-1]
        
        # Прокручиваем к кнопке
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        time.sleep(0.5)
        order_button.click()
        
        # Подтверждение "Да"
        yes_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']"))
        )
        yes_button.click()
    
    def get_success_message(self):
        """Получение сообщения об успешном создании заказа"""
        success_msg = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'Order_ModalHeader') or contains(text(), 'Заказ оформлен')]"))
        )
        return success_msg.text


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MainPage:
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FourPart')]")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def click_order_button_top(self):
        """Клик по кнопке Заказать вверху страницы"""
        button = self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON_TOP))
        button.click()
    
    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    
        all_buttons = self.driver.find_elements(By.XPATH, "//button[text()='Заказать']")
        bottom_button = all_buttons[-1]
    
    # Клик через JavaScript
        self.driver.execute_script("arguments[0].click();", bottom_button)

    
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.driver.find_element(*self.SCOOTER_LOGO).click()
    
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.driver.find_element(*self.YANDEX_LOGO).click()

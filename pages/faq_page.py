from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FAQPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def get_faq_question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")
    
    def get_faq_answer_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")
    
    def click_faq_question(self, index):
        """Клик по вопросу с прокруткой и использованием JavaScript"""
        question = self.wait.until(
            EC.presence_of_element_located(self.get_faq_question_locator(index))
        )
        # Прокрутка элемента в видимую область
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        # Небольшая задержка для завершения прокрутки
        self.wait.until(EC.element_to_be_clickable(self.get_faq_question_locator(index)))
        # Клик через JavaScript для избежания перекрытия
        self.driver.execute_script("arguments[0].click();", question)
    
    def get_faq_answer_text(self, index):
        """Получение текста ответа"""
        answer = self.wait.until(
            EC.visibility_of_element_located(self.get_faq_answer_locator(index))
        )
        return answer.text

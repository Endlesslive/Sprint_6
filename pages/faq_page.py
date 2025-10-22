from locators.page_locators import FAQPageLocators
from pages.base_page import BasePage

class FAQPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def scroll_to_faq_section(self):
        """Прокрутка к разделу FAQ"""
        self.scroll_to_element(FAQPageLocators.FAQ_SECTION, block='start')
    
    def click_faq_question(self, index):
        """Клик по вопросу"""
        question_locator = FAQPageLocators.get_faq_question_locator(index)
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
    
    def get_faq_answer_text(self, index):
        """Получение текста ответа"""
        answer_locator = FAQPageLocators.get_faq_answer_locator(index)
        return self.get_element_text(answer_locator)
    
    def is_answer_visible(self, index):
        """Проверка видимости ответа"""
        answer_locator = FAQPageLocators.get_faq_answer_locator(index)
        return self.is_element_visible(answer_locator)
    
    def get_question_text(self, index):
        """Получение текста вопроса"""
        question_locator = FAQPageLocators.get_faq_question_locator(index)
        return self.get_element_text(question_locator)

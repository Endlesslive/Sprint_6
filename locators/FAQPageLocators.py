from selenium.webdriver.common.by import By

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
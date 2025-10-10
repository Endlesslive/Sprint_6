import pytest
import allure
from pages.main_page import MainPage
from pages.faq_page import FAQPage

class TestFAQSection:
    
    @pytest.mark.parametrize("question_index,expected_text", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат"),
        (2, "Допустим, вы оформляете заказ на 8 мая"),
        (3, "Только начиная с завтрашнего дня"),
        (4, "Пока что нет"),
        (5, "Самокат приезжает к вам с полной зарядкой"),
        (6, "Да, пока самокат не привезли"),
        (7, "Да, обязательно")
    ])
    @allure.title("Проверка раскрытия вопроса {question_index} в разделе FAQ")
    @allure.description("Тест проверяет открытие ответа при клике на вопрос")
    def test_faq_question_answer(self, driver, question_index, expected_text):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        
        faq_page = FAQPage(driver)
        faq_page.click_faq_question(question_index)
        answer_text = faq_page.get_faq_answer_text(question_index)
        
        assert expected_text in answer_text

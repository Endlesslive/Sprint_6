import pytest
import allure


class TestFAQSection:
    FAQ_TEST_DATA = [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат"),
        (2, "Допустим, вы оформляете заказ на 8 мая"),
        (3, "Только начиная с завтрашнего дня"),
        (4, "Пока что нет"),
        (5, "Самокат приезжает к вам с полной зарядкой"),
        (6, "Да, пока самокат не привезли"),
        (7, "Да, обязательно")
    ]
    
    @pytest.mark.parametrize("question_index,expected_text", FAQ_TEST_DATA)
    @allure.feature("Раздел FAQ")
    @allure.story("Проверка вопросов и ответов")
    @allure.title("Проверка раскрытия вопроса #{question_index} в разделе FAQ")
    @allure.description("Тест проверяет открытие ответа при клике на вопрос и корректность текста ответа")
    def test_faq_question_answer(self, faq_page, question_index, expected_text):
        """Проверка открытия ответа при клике на вопрос"""
        with allure.step(f"Прокручиваем к разделу FAQ"):
            faq_page.scroll_to_faq_section()
        with allure.step(f"Кликаем на вопрос #{question_index}"):
            faq_page.click_faq_question(question_index)
        with allure.step(f"Проверяем, что ответ стал видимым"):
            assert faq_page.is_answer_visible(question_index), \
                f"Ответ на вопрос {question_index} не отображается"
        with allure.step(f"Получаем текст ответа"):
            answer_text = faq_page.get_faq_answer_text(question_index)
        with allure.step(f"Проверяем корректность текста ответа"):
            assert expected_text in answer_text, \
                f"Ожидаемый текст '{expected_text}' не найден в ответе: '{answer_text}'"

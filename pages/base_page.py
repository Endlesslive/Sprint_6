from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def find_element(self, locator):
        """Поиск элемента с ожиданием его присутствия"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Элемент {locator} не найден на странице")
    
    def find_elements(self, locator):
        """Поиск всех элементов по локатору"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise Exception(f"Элементы {locator} не найдены на странице")
    
    def click_element(self, locator):
        """Клик по элементу с ожиданием его кликабельности"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
        except TimeoutException:
            raise Exception(f"Элемент {locator} не стал кликабельным")
    
    def enter_text(self, locator, text):
        """Ввод текста в поле"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            raise Exception(f"Не удалось ввести текст в элемент {locator}")
    
    def get_element_text(self, locator):
        """Получение текста элемента"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            raise Exception(f"Не удалось получить текст элемента {locator}")
    
    def is_element_visible(self, locator):
        """Проверка видимости элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator):
        """Проверка присутствия элемента в DOM"""
        try:
            self.find_element(locator)
            return True
        except:
            return False
    
    def scroll_to_element(self, locator, behavior='smooth', block='center'):
        """Прокрутка к элементу"""
        try:
            element = self.find_element(locator)
            self.driver.execute_script(
                f"arguments[0].scrollIntoView({{behavior: '{behavior}', block: '{block}'}});",
                element
            )
            self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            raise Exception(f"Не удалось прокрутить к элементу {locator}: {str(e)}")
    
    def scroll_to_top(self):
        """Прокрутка в начало страницы"""
        self.driver.execute_script("window.scrollTo(0, 0);")
    
    def scroll_to_bottom(self):
        """Прокрутка в конец страницы"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def wait_for_element_to_disappear(self, locator):
        """Ожидание исчезновения элемента"""
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Элемент {locator} не исчез со страницы")
    
    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Получение заголовка страницы"""
        return self.driver.title
    
    def wait_for_new_window(self, expected_windows_count, timeout=10):
        """Ожидание открытия нового окна"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.number_of_windows_to_be(expected_windows_count))
        except TimeoutException:
            raise Exception(f"Не дождались открытия нового окна. Ожидалось {expected_windows_count} окон")
    
    def switch_to_new_window(self, original_window):
        """Переключение на новое окно"""
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
    
    def wait_for_url_change(self, timeout=10):
        """Ожидание изменения URL с about:blank"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda d: d.current_url != "about:blank")
        except TimeoutException:
            raise Exception("URL не изменился с about:blank")
    
    def wait_for_url_contains(self, text, timeout=10):
        """Ожидание, что URL содержит определённый текст"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda d: text in d.current_url)
            return True
        except TimeoutException:
            return False
    
    def get_window_handle(self):
        """Получение текущего window handle"""
        return self.driver.current_window_handle

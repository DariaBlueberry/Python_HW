import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (
            By.XPATH, "//div[@class='inventory_item_price summary_total_label']"
        )

    def _find_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ввести имя '{first_name}'")
    def enter_first_name(self, first_name: str):
        """Вводит имя в поле 'First Name'.

        :param first_name: Имя покупателя.
        """
        field = self._find_element(self.first_name_input)
        field.clear()
        field.send_keys(first_name)

    @allure.step("Ввести фамилию '{last_name}'")
    def enter_last_name(self, last_name: str):
        """Вводит фамилию в поле 'Last Name'.

        :param last_name: Фамилия покупателя.
        """
        field = self._find_element(self.last_name_input)
        field.clear()
        field.send_keys(last_name)

    @allure.step("Ввести почтовый индекс '{postal_code}'")
    def enter_postal_code(self, postal_code: str):
        """Вводит почтовый индекс.

        :param postal_code: Почтовый индекс.
        """
        field = self._find_element(self.postal_code_input)
        field.clear()
        field.send_keys(postal_code)

    @allure.step("Нажать кнопку 'Continue'")
    def click_continue(self):
        """Кликает по кнопке продолжения."""
        button = self._find_element(self.continue_button)
        button.click()

    @allure.step("Получить итоговую сумму")
    def get_total(self) -> str:
        """Возвращает текст итоговой суммы."""
        total_element = self._find_element(self.total_label)
        return total_element.text

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Checkout_Info:

    def __init__(self, driver):
        self._driver = driver
        chrome_options = Options()
        (chrome_options.add_experimental_option
         ("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
         }))

    def first_name(self):
        first_name_input = (
            WebDriverWait(self._driver, 10)
            .until(EC.presence_of_element_located((By.ID, "first-name")))
        )
        first_name_input.send_keys("Иван")

    def last_name(self):
        last_name_input = self._driver.find_element(By.ID, "last-name")
        last_name_input.send_keys("Петров")

    def postal_code(self):
        postal_code_input = self._driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys("1234566666")

    def continue_button(self):
        continue_button = self._driver.find_element(By.ID, "continue")
        continue_button.click()

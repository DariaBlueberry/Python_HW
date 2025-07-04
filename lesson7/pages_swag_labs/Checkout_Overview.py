from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Checkout_Overview:

    def __init__(self, driver):
        self._driver = driver
        chrome_options = Options()
        (chrome_options.add_experimental_option
         ("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False}))

    def total_element(self):
        total_element = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_price_text = total_element.text
        return total_price_text

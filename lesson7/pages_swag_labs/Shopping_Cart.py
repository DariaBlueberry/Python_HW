from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Shopping_Cart:

    def __init__(self, driver):
        self._driver = driver
        chrome_options = Options()
        (chrome_options.add_experimental_option
         ("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False}))

    def checkout_button(self):
        checkout_button = WebDriverWait(self._driver, 10).until(
                          EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Authorization:
    def __init__(self, driver):
        chrome_options = Options()
        (chrome_options.add_experimental_option
         ("prefs", {
             "credentials_enable_service": False,
             "profile.password_manager_enabled": False
         }
         ))
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def user_name(self):
        username_input = self._driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")

    def password(self):
        password_input = self._driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")

    def login_button(self):
        login_button = self._driver.find_element(By.ID, "login-button")
        login_button.click()

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы входа.
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу входа")
    def open(self):
        """
        Открывает страницу входа на сайт saucedemo.com.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str):
        """
        Вводит имя пользователя в поле логина.
        """
        username_field = self.driver.find_element(*self.username_input)
        username_field.send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str):
        """
        Вводит пароль в поле пароля.
        """
        password_field = self.driver.find_element(*self.password_input)
        password_field.send_keys(password)

    def click_login(self):
        """
        Нажимает кнопку входа для авторизации.
        """
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

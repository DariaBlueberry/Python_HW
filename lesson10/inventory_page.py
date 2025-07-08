import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы инвентаря.

        :param driver: Объект WebDriver для взаимодействия с браузером.
        """
        self.driver = driver
        self.add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_tshirt_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie_button = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self):
        """
        Нажимает кнопку добавления рюкзака в корзину и ожидает обновления значка корзины.
        """
        backpack_button = self.driver.find_element(*self.add_backpack_button)
        backpack_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "shopping_cart_badge"),
                "1",
            )
        )

    @allure.step("Добавить футболку в корзину")
    def add_tshirt_to_cart(self):
        """
        Нажимает кнопку добавления футболки в корзину.
        """
        tshirt_button = self.driver.find_element(*self.add_tshirt_button)
        tshirt_button.click()

    @allure.step("Добавить майку Onesie в корзину")
    def add_onesie_to_cart(self):
        """
        Нажимает кнопку добавления майки Onesie в корзину.
        """
        onesie_button = self.driver.find_element(*self.add_onesie_button)
        onesie_button.click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Переходит на страницу корзины, кликая по ссылке корзины.
        """
        cart_link = self.driver.find_element(*self.cart_link)
        cart_link.click()

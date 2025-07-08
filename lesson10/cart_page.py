from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class CartPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины.
        :param driver: Объект WebDriver для взаимодействия с браузером.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.backpack_in_cart = (
            By.XPATH,
            "//div[@class='cart_item'][.//div[contains(text(), "
            "'Sauce Labs Backpack')]]",
        )
        self.tshirt_in_cart = (
            By.XPATH,
            "//div[@class='cart_item'][.//div[contains(text(), "
            "'Sauce Labs Bolt T-Shirt')]]",
        )
        self.onesie_in_cart = (
            By.XPATH,
            "//div[@class='cart_item'][.//div[contains(text(), "
            "'Sauce Labs Onesie')]]",
        )

    def click_checkout(self):
        """
        Нажимает на кнопку 'Checkout' для перехода к оформлению заказа.
        """
        checkout_button = self.driver.find_element(*self.checkout_button)
        checkout_button.click()

    def is_backpack_in_cart(self):
        """
        Проверяет наличие товара 'Sauce Labs Backpack' в корзине.
        :return: True, если товар есть в корзине; False — если отсутствует.
        """
        try:
            self.driver.find_element(*self.backpack_in_cart)
            return True
        except NoSuchElementException:
            return False

    def is_tshirt_in_cart(self):
        """
        Проверяет наличие товара 'Sauce Labs Bolt T-Shirt' в корзине.

        :return: True, если товар есть в корзине; False — если отсутствует.
        """
        try:
            self.driver.find_element(*self.tshirt_in_cart)
            return True
        except NoSuchElementException:
            return False

    def is_onesie_in_cart(self):
        """
        Проверяет наличие товара 'Sauce Labs Onesie' в корзине.

        :return: True, если товар есть в корзине; False — если отсутствует.
        """
        try:
            self.driver.find_element(*self.onesie_in_cart)
            return True
        except NoSuchElementException:
            return False

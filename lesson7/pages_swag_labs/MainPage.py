from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class MainPage:

    def __init__(self, driver):
        self._driver = driver
        chrome_options = Options()
        (chrome_options.add_experimental_option
         ("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False}))

    def add_backpack(self):
        backpack_button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, "add-to-cart-sauce-labs-backpack")))
        backpack_button.click()

    def add_tshirt(self):
        tshirt_button = self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_button.click()

    def add_onesie(self):
        onesie_button = self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_button.click()

    def cart_link(self):
        cart_link = self._driver.find_element(By.CLASS_NAME,
                                              "shopping_cart_link")
        cart_link.click()

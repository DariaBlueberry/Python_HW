from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Calculator:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-'
                         'webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(6)
        self._driver.maximize_window()

    def delay_input(self, num):
        # поле ввода
        delay_input = self._driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(num)

    def button_7(self):
        button_7 = self._driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

    def button_8(self):
        button_8 = self._driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()

    def button_plus(self):
        button_plus = self._driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

    def button_equals(self):
        button_equals = self._driver.find_element(By.XPATH,
                                                  "//span[text()='=']")
        button_equals.click()

    def result_display(self):
        result_display = WebDriverWait(self._driver, 46).until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "screen"), "15"))
        return result_display

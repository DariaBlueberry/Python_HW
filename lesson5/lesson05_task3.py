from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/inputs')

driver.maximize_window()

search_locator = 'input'

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)


search_input.send_keys('Sky')  # Отправить значение в строку поиск


search_input.send_keys(Keys.RETURN)  # как нажать кнопку Enter через команду
sleep(2)
try:
    success_element = driver.find_element(By.ID, "id")
    print("Отправка прошла успешно.")
except NoSuchElementException:
    print("Не удалось отправить 'Sky'")

search_input.clear()

search_input.send_keys('Pro')  # Отправить значение в строку поиск

search_input.send_keys(Keys.RETURN)  # как нажать кнопку Enter через команду
sleep(2)
try:
    success_element = driver.find_element(By.ID, "id")
    print("Отправка прошла успешно.")
except NoSuchElementException:
    print("Не удалось отправить 'Pro'")

search_input.clear()
sleep(2)


driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/textinput')

search_locator = 'input'

search_input = driver.find_element(By.CSS_SELECTOR, search_locator)


search_input.send_keys('SkyPro')  # Отправить значение в строку поиск

blue_button = driver.find_element(By.CSS_SELECTOR,
                                  "button.btn.btn-primary")
blue_button.click()
time.sleep(1)

button_text = blue_button.text

print(f'("{button_text}")')

driver.quit()

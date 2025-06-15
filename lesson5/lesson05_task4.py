from time import sleep
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/login')

search_username = '#username'
search_input = driver.find_element(By.CSS_SELECTOR, search_username)


search_input.send_keys('tomsmith')  # Отправить значение в строку поиск


search_password = '#password'


search_input = driver.find_element(By.CSS_SELECTOR, search_password)
search_input.send_keys('SuperSecretPassword!')
# Отправить значение в строку поиск

search_input.send_keys(Keys.RETURN)  # как нажать кнопку Enter через команду
try:
    success_element = driver.find_element(By.ID, "flash-messages")
    print("You logged into a secure area!")
except NoSuchElementException:
    print("Не удалось войти в личный кабинет")
sleep(2)

driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/dynamicid')

driver.maximize_window()

dynamic_id_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

dynamic_id_button.click()
print("Кнопка нажата успешно")

sleep(2)

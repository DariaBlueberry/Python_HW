from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/classattr')

driver.maximize_window()

blue_button = driver.find_element(By.CSS_SELECTOR,
                                  "button.btn-primary.btn-test")

blue_button.click()
print("Кнопка нажата успешно")

sleep(2)

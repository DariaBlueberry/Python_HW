from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('http://uitestingplayground.com/ajax')

blue_button = driver.find_element(By.CSS_SELECTOR,
                                  "button.btn.btn-primary")

blue_button.click()
try:
    success_element = driver.find_element(By.CLASS_NAME, "bg-success")
    print("Data loaded with AJAX get request.")
except NoSuchElementException:
    print("Не удалось выполнить")

driver.quit()

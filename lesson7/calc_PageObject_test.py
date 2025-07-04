
from selenium import webdriver

from lesson7.Calculator import Calculator


def test_calc():
    browser = webdriver.Chrome()

    calc = Calculator(browser)
    calc.delay_input(45)
    calc.button_7()
    calc.button_plus()
    calc.button_8()
    calc.button_equals()
    calc.result_display()

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from lesson7.pages_swag_labs.Authorization import Authorization
from lesson7.pages_swag_labs.MainPage import MainPage
from lesson7.pages_swag_labs.Shopping_Cart import Shopping_Cart
from lesson7.pages_swag_labs.Checkout_Info import Checkout_Info
from lesson7.pages_swag_labs.Checkout_Overview import Checkout_Overview

chrome_options = Options()
(chrome_options.add_experimental_option
 ("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False}))


def test_swag_labs():
    browser = webdriver.Chrome(options=chrome_options)
    # Авторизация на сайте
    log_in = Authorization(browser)
    log_in.user_name()
    log_in.password()
    log_in.login_button()

    # Внести товары в корзину и открыть корзину
    shopping = MainPage(browser)
    shopping.add_backpack()
    shopping.add_onesie()
    shopping.add_tshirt()
    shopping.cart_link()

    check = Shopping_Cart(browser)
    check.checkout_button()

    check_info = Checkout_Info(browser)
    check_info.first_name()
    check_info.last_name()
    check_info.postal_code()
    check_info.continue_button()

    check_overwiew = Checkout_Overview(browser)
    check_overwiew.total_element()

    expected_total = "Total: $58.29"
    total_element = check_overwiew.total_element()
    total_price_text = total_element

    assert total_price_text == expected_total, (
        f"Итоговая сумма '{total_price_text}' не соответствует "
        f"ожидаемой '{expected_total}'"
    )
    browser.quit()

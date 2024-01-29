from selenium.webdriver.common.by import By
import time


def test_check_buy_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    btn = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert btn is not None, 'нет кнопки'

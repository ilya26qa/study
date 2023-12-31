from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    selector_value = '#input_value'
    x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    x = x_element.text
    y = calc(x)

    # Отправляем заполненную форму
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
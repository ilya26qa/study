from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
browser.find_element(By.ID,'book').click()
# time.sleep(30)

count = browser.find_element(By.ID, 'input_value').text

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(calc(int(count)))
browser.find_element(By.ID,'solve').click()
time.sleep(10)
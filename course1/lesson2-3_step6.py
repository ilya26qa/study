from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.ID, 'input_value').text
count = calc(x)


input = browser.find_element(By.ID, "answer")
input.send_keys(count)

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
print(browser.switch_to.alert.text)
time.sleep(5)

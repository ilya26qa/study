from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

img = browser.find_element(By.CSS_SELECTOR, 'img')
x = img.get_attribute("valuex")
count = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(count)

checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox.click()

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_radio.click()

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(20)

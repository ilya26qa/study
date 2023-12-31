from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
alert = browser.switch_to.alert
alert.accept()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x = browser.find_element(By.ID, 'input_value').text
count = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(count)


button = browser.find_element(By.CLASS_NAME, "btn")
button.click()
time.sleep(20)

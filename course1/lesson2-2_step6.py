from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, 'input_value').text


input = browser.find_element(By.CLASS_NAME, 'form-control')
input.send_keys(str(calc(num1)))

checkbox = browser.find_element(By.ID, 'robotCheckbox')
checkbox.click()

radio = browser.find_element(By.ID, 'robotsRule')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element(By.CLASS_NAME, "btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


print(browser.switch_to.alert.text)
time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.ID, 'num1').text
num2 = browser.find_element(By.ID, 'num2').text

sum = int(num1) + int(num2)

select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
select.select_by_value(str(sum))



button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

print(browser.switch_to.alert.text)
time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)


input = browser.find_element(By.NAME, "firstname")
input.send_keys('ilya')

input = browser.find_element(By.NAME, "lastname")
input.send_keys('ilya')

input = browser.find_element(By.NAME, "email")
input.send_keys('ilya@mail.ry')


file = browser.find_element(By.NAME, 'file')
file.send_keys('/Users/ilya/Documents/study/course1/text.txt')

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(20)

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

time.sleep(5)
# Закрытие браузера
driver.quit()
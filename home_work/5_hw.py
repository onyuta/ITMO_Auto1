from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
# Поиск элементов
username_field = driver.find_element(By.ID, 'user-name')
password_field = driver.find_element(By.ID, 'password')
submit_button = driver.find_element(By.ID, 'login-button')

if username_field and password_field and submit_button:
    print('Элементы найдены')

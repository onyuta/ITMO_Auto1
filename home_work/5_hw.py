from selenium import webdriver
from selenium.webdriver.common.by import By

def find_elements_on_page():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')
    submit_button = driver.find_element(By.ID, 'login-button')

    print('Элементы найдены')
    return True

find_elements_on_page()
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_exp(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable((By.ID, 'startTest')))
    driver.find_element(By.ID, 'startTest').click()
    driver.find_element(By.ID, 'login').send_keys('login')
    driver.find_element(By.ID, 'password').send_keys('password')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()
    element = driver.find_element(By.ID, 'loader')
    if element.is_displayed():
        print('Element is visible!')
    else:
        print('Element is not visible!')
    assert driver.find_element(By.XPATH, '//body//h1').text == 'Практика с ожиданиями в Selenium'
    wait.until(ec.visibility_of_element_located((By.ID, 'successMessage')))
    element2 = driver.find_element(By.ID, 'successMessage')
    if element2.is_displayed():
        print('Element2 is visible!')
    else:
        print('Element2 is not visible!')
    assert element2.text == 'Вы успешно зарегистрированы!'


def test_imp(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    assert driver.find_element(By.XPATH, '//body//h1').text == 'Практика с ожиданиями в Selenium'
    driver.find_element(By.ID, 'startTest').click()
    driver.find_element(By.ID, 'login').send_keys('login')
    driver.find_element(By.ID, 'password').send_keys('password')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()
    element = driver.find_element(By.ID, 'loader')
    if element.is_displayed():
        print('Element is visible!')
    else:
        print('Element is not visible!')
    time.sleep(5)
    element2 = driver.find_element(By.ID, 'successMessage')
    if element2.is_displayed():
        print('Element2 is visible!')
    else:
        print('Element2 is not visible!')
    assert element2.text == 'Вы успешно зарегистрированы!'


def test_add_del_elem(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    driver.find_element(By.XPATH, '//button').click()
    element = driver.find_element(By.XPATH, "//*[@class='added-manually']")
    if element.is_displayed():
        print('Element is present!')
    else:
        print('Element is NOT present!')
    assert element.text == 'Delete'
    element.click()
    driver.quit()

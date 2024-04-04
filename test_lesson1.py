import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
correct_login = 'standard_user'
correct_password = 'secret_sauce'


def test_login_page():
    login()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'
    browser.quit()


def test_login_page_incorrect():
    browser.get(base_url)
    browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys('standart_user')
    browser.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sau')
    browser.find_element(By.XPATH, "//input[@id='login-button']").click()
    assert browser.find_element(By.XPATH,
                                "//h3[@data-test='error']").text == 'Epic sadface: Username and password do not match any user in this service'
    # assert browser.current_url == 'https://www.saucedemo.com/', 'url не соответствует ожиданиям'
    browser.quit()


def test_add_item():
    login()
    add_to_cart()
    assert browser.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Backpack'


def test_add_item_from_card():
    login()
    browser.find_element(By.XPATH, "//a[@id='item_0_title_link']").click()
    browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
    assert browser.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Bike Light'


def test_delete_item_from_card():
    login()
    browser.find_element(By.XPATH, "//a[@id='item_0_title_link']").click()
    browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    browser.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']").click()
    assert browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").text == 'Add to cart'


def test_delete_item():
    login()
    add_to_cart()
    browser.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()
    assert browser.find_element(By.XPATH, "//button[@id='continue-shopping']").text == 'Continue Shopping'


def test_card_item_picture():
    login()
    browser.find_element(By.XPATH, "//a[@id='item_1_img_link']").click()
    assert browser.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").text == 'Sauce Labs Bolt T-Shirt'


def test_card_item_name():
    login()
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[@id='item_1_title_link']").click()
    assert browser.find_element(By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']").text == 'Sauce Labs Bolt T-Shirt'


def test_filter_a():
    login()
    browser.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[@value='az']").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH,
                                "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Backpack'


def test_filter_z():
    login()
    browser.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[@value='za']").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH,
                                "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Test.allTheThings() T-Shirt (Red)'


def test_filter_low():
    login()
    browser.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[@value='lohi']").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH,
                                "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Onesie'


def test_filter_high():
    login()
    browser.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//option[@value='hilo']").click()
    time.sleep(2)
    assert browser.find_element(By.XPATH,
                                "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Fleece Jacket'


def test_logout():
    login()
    browser.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
    # assert browser.find_element(By.XPATH, "//input[@id='login-button']"). == ''???
    browser.quit()


def test_about():
    login()
    browser.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[@id='about_sidebar_link']").click()
    assert browser.current_url == 'https://saucelabs.com/', 'url не соответствует ожидаемому'
    browser.quit()


def test_reset():
    login()
    browser.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[@id='reset_sidebar_link']").click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'
    browser.quit()


def add_to_cart():
    browser.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()


def login():
    browser.get(base_url)
    browser.find_element(By.XPATH, "//input[@id='user-name']").send_keys(correct_login)
    browser.find_element(By.XPATH, "//input[@id='password']").send_keys(correct_password)
    browser.find_element(By.XPATH, "//input[@id='login-button']").click()



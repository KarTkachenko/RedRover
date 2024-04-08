from selenium.webdriver.common.by import By


class CartPage:
    base_url = 'https://www.saucedemo.com/'

    # locators
    _shopping_cart = "//*[@id='shopping_cart_container']"
    _add_to_cart_in = "//button[@id='add-to-cart']"
    _add_to_cart_out = '//button[@id="add-to-cart-sauce-labs-backpack"]'

    def cart_container(self, driver):
        driver.find_element(By.XPATH, self._shopping_cart).click()

    def add_to_cart_inside(self, driver):
        driver.find_element(By.XPATH, self._add_to_cart_in).click()

    def add_to_cart(self, driver):
        driver.find_element(By.XPATH, self._add_to_cart_out).click()

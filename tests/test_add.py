
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from conftest import driver
from pages.cart_page import CartPage


class TestAdd:
    cp = CartPage()
    bp = BasePage()

    # locators
    _text_check = "//div[@class='inventory_item_name']"

    def test_add_item(self, driver):
        self.bp.login(driver)
        self.cp.add_to_cart(driver)
        self.cp.cart_container(driver)
        assert driver.find_element(By.XPATH, self._text_check).text == 'Sauce Labs Backpack'

    def test_add_item_from_card(self, driver):
        self.bp.login(driver)
        self.cp.add_to_cart_inside(driver)
        self.cp.cart_container(driver)
        assert driver.find_element(By.XPATH, self._text_check).text == 'Sauce Labs Bike Light'

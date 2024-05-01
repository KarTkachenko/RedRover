from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.cart_page import CartPage


class TestAdd:
    cp = CartPage()
    bp = BasePage()

    def test_add_item(self, driver):
        self.bp.login(driver)
        self.cp.add_to_cart(driver)
        self.cp.cart_container(driver)
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Backpack'

    def test_add_item_from_card(self, driver):
        self.bp.login(driver)
        self.cp.add_to_cart_inside(driver)
        self.cp.cart_container(driver)
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Bike Light'

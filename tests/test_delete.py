import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestDelete:
    bp = BasePage()

    def test_delete_item_from_card(self, driver):
        self.bp.login(driver)
        self.bp.partic_item(driver)
        self.bp.add_to_cart_inside(driver)
        self.bp.remove_item(driver)
        assert driver.find_element(By.XPATH, "//button[@id='add-to-cart']").text == 'Add to cart'

    def test_delete_item(self, driver):
        self.bp.login(driver)
        self.bp.add_to_cart(driver)
        self.bp.remove_part_item(driver)
        self.bp.put_to_cart(driver)
        assert driver.find_element(By.XPATH, "//button[@id='continue-shopping']").text == 'Continue Shopping'


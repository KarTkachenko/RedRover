from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestAdd:
    bp = BasePage()

    def test_add_item(self, driver):
        self.bp.login(driver)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        self.bp.put_to_cart(driver)
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Backpack'

    def test_add_item_from_card(self, driver):
        self.bp.login(driver)
        self.bp.partic_item(driver)
        self.bp.add_to_cart(driver)
        self.bp.put_to_cart(driver)
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Bike Light'

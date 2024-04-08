from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestItems:
    bp = BasePage()

    def test_card_item_picture(self, driver):
        self.bp.login(driver)
        self.bp.image_item(driver)
        assert driver.find_element(By.XPATH,
                                   "//div[text()='Sauce Labs Bolt T-Shirt']").text == 'Sauce Labs Bolt T-Shirt'

    def test_card_item_name(self, driver):
        self.bp.login(driver)
        self.bp.name_item(driver)
        assert driver.find_element(By.XPATH,
                                   "//div[text()='Sauce Labs Bolt T-Shirt']").text == 'Sauce Labs Bolt T-Shirt'

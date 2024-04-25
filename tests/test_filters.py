from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.filters import Sort


class TestFilter:
    bp = BasePage()
    s = Sort()

    def test_filter_a(self, driver):
        self.bp.login(driver)
        self.s.sort_filter(driver)
        self.s.filter_a_z(driver)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Backpack'

    def test_filter_z(self, driver):
        self.bp.login(driver)
        self.s.sort_filter(driver)
        self.s.filter_z_a(driver)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Test.allTheThings() T-Shirt (Red)'

    def test_filter_low(self, driver):
        self.bp.login(driver)
        self.s.sort_filter(driver)
        self.s.filter_low(driver)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Onesie'

    def test_filter_high(self, driver):
        self.bp.login(driver)
        self.s.sort_filter(driver)
        self.s.filter_high(driver)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Fleece Jacket'

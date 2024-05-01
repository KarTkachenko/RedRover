import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class Test:
    bp = BasePage()

    def test_logout(self, driver):
        self.bp.login(driver)
        self.bp.burger_menu(driver)
        time.sleep(1)
        self.bp.logout(driver)
        time.sleep(1)
        assert 'Accepted usernames are:' in driver.find_element(By.XPATH, "//div[@id='login_credentials']").text

    def test_about(self, driver):
        self.bp.login(driver)
        self.bp.burger_menu(driver)
        time.sleep(1)
        self.bp.about(driver)
        assert driver.current_url == 'https://saucelabs.com/', 'url не соответствует ожидаемому'

    def test_reset(self, driver):
        self.bp.login(driver)
        self.bp.burger_menu(driver)
        time.sleep(1)
        self.bp.reset(driver)
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

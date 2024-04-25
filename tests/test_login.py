from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TestLogin:
    bp = BasePage()

    # locators
    _error = "//h3[@data-test='error']"

    def test_login_page(self, driver):
        self.bp.login(driver)
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    def test_login_page_incorrect(self, driver):
        self.bp.login(driver, login='standart', password='sause')
        assert driver.find_element(By.XPATH,
                                   self._error).text == ('Epic sadface: Username and password do not '
                                                         'match any user in this service')

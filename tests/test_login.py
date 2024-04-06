from selenium.webdriver.common.by import By
from pages.base_page import BasePage as bp


class TestLogin:
    new = bp()

    # locators
    _error = "//h3[@data-test='error']"

    def test_login_page(self, driver):
        self.new.login(driver)
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    def test_login_page_incorrect(self, driver):
        self.new.login(driver, 'standart_user', 'secret_sau')
        assert driver.find_element(By.XPATH,
                                   self._error).text == ('Epic sadface: Username and password do not '
                                                         'match any user in this service')

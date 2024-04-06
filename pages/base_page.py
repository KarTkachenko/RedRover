from selenium.webdriver.common.by import By


class BasePage:
    base_url = 'https://www.saucedemo.com/'

    # locators
    _username = "//input[@id='user-name']"
    _password = "//input[@id='password']"
    _login_button = "//input[@id='login-button']"

    def login(self, driver, login='standard_user', password='secret_sauce'):
        driver.get(self.base_url)
        driver.find_element(By.XPATH, self._username).send_keys(login)
        driver.find_element(By.XPATH, self._password).send_keys(password)
        driver.find_element(By.XPATH, self._login_button).click()

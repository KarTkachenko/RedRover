from selenium.webdriver.common.by import By


class BasePage:

    _username = "//input[@id='user-name']"
    _password = "//input[@id='password']"
    _login_button = "//input[@id='login-button']"
    _item = "//a[@id='item_0_title_link']"
    _burger_menu = "//button[@id='react-burger-menu-btn']"
    _remove = "//button[@id='remove']"
    _remove_p_item = "//button[@id='remove-sauce-labs-backpack']"
    _image = "//a[@id='item_1_img_link']"
    _name = "//a[@id='item_1_title_link']"
    _logout = "//a[@id='logout_sidebar_link']"
    _about = "//a[@id='about_sidebar_link']"
    _reset = "//a[@id='reset_sidebar_link']"

    def login(self, driver, login='standard_user', password='secret_sauce'):
        driver.find_element(By.XPATH, self._username).send_keys(login)
        driver.find_element(By.XPATH, self._password).send_keys(password)
        driver.find_element(By.XPATH, self._login_button).click()

    def partic_item(self, driver):
        driver.find_element(By.XPATH, self._item).click()

    def burger_menu(self, driver):
        driver.find_element(By.XPATH, self._burger_menu).click()

    def remove_item(self, driver):
        driver.find_element(By.XPATH, self._remove).click()

    def remove_part_item(self, driver):
        driver.find_element(By.XPATH, self._remove_p_item).click()

    def image_item(self, driver):
        driver.find_element(By.XPATH, self._image).click()

    def name_item(self, driver):
        driver.find_element(By.XPATH, self._name).click()

    def logout(self, driver):
        driver.find_element(By.XPATH, self._logout).click()

    def about(self, driver):
        driver.find_element(By.XPATH, self._about).click()

    def reset(self, driver):
        driver.find_element(By.XPATH, self._reset).click()

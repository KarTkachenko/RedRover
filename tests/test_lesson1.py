import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage as bp


class Test:

    def test_add_item(self, driver):
        bp.login(driver)
        self.add_to_cart(driver)
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Backpack'

    def test_add_item_from_card(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//a[@id='item_0_title_link']").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()
        driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
        assert driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text == 'Sauce Labs Bike Light'

    def test_delete_item_from_card(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//a[@id='item_0_title_link']").click()
        driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click()
        driver.find_element(By.XPATH, "//button[@id='remove']").click()
        assert driver.find_element(By.XPATH, "//button[@id='add-to-cart']").text == 'Add to cart'

    def test_delete_item(self, driver):
        self.login(driver)
        self.add_to_cart(driver)
        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']").click()
        assert driver.find_element(By.XPATH, "//button[@id='continue-shopping']").text == 'Continue Shopping'

    def test_card_item_picture(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//a[@id='item_1_img_link']").click()
        assert driver.find_element(By.XPATH,
                                   "//div[text()='Sauce Labs Bolt T-Shirt']").text == 'Sauce Labs Bolt T-Shirt'

    def test_card_item_name(self, driver):
        self.login(driver)
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='item_1_title_link']").click()
        assert driver.find_element(By.XPATH,
                                   "//div[text()='Sauce Labs Bolt T-Shirt']").text == 'Sauce Labs Bolt T-Shirt'

    def test_filter_a(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[@value='az']").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Backpack'

    def test_filter_z(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[@value='za']").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Test.allTheThings() T-Shirt (Red)'

    def test_filter_low(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[@value='lohi']").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Onesie'

    def test_filter_high(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//option[@value='hilo']").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,
                                   "//div[@class='inventory_list']/div[1]//div[contains(@class,'inventory_item_name')]").text == 'Sauce Labs Fleece Jacket'

    def test_logout(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        # assert browser.find_element(By.XPATH, "//input[@id='login-button']"). == ''???

    def test_about(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']").click()
        assert driver.current_url == 'https://saucelabs.com/', 'url не соответствует ожидаемому'

    def test_reset(self, driver):
        self.login(driver)
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@id='reset_sidebar_link']").click()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'url не соответствует ожидаемому'

    @staticmethod
    def add_to_cart(driver):
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()

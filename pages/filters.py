from selenium.webdriver.common.by import By


class Sort:
    # locators
    _filter = "//select[@class='product_sort_container']"
    _az = "//option[@value='az']"
    _za = "//option[@value='za']"
    _low = "//option[@value='lohi']"
    _high = "//option[@value='hilo']"

    def sort_filter(self, driver):
        driver.find_element(By.XPATH, self._filter).click()

    def filter_a_z(self, driver):
        driver.find_element(By.XPATH, self._az).click()

    def filter_z_a(self, driver):
        driver.find_element(By.XPATH, self._za).click()

    def filter_low(self, driver):
        driver.find_element(By.XPATH, self._low).click()

    def filter_high(self, driver):
        driver.find_element(By.XPATH, self._high).click()

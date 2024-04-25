import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

base_url = 'https://www.saucedemo.com/'


@pytest.fixture
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    driver.quit()

import pytest
from selenium import webdriver


base_url = 'https://www.saucedemo.com/'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='module')
def messages():
    print('Start')
    yield
    print('Stop!!!')

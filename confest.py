import pytest
from selenium import webdriver

baseUrl = 'https://www.soglasie.ru/'


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

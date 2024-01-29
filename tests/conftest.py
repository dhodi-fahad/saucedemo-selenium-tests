from selenium import webdriver

import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    yield driver

import pytest
from selenium import webdriver
from data import *
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get(URL.main_page_url)
    yield driver
    driver.quit()

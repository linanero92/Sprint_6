import allure
from data import *
from conftest import *
from pages.main_page import MainPage
import pytest

class TestScooterYandexLogo:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()










    def test_scooter_logo(self):
        self.driver.get(URL.main_page_url)
        main_page = MainPage(self.driver)

        expected_result = main_page.get_main_page_via_scooter_logo()

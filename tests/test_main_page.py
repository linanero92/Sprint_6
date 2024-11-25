import pytest
import allure
from data import *
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title('Тестирование получения ответов на вопросы о важном')
    @allure.description('Тестирование получения ответов на вопросы о важном')
    @pytest.mark.parametrize('num, expected_answer', [
        (0, Answers.Answer_0),
        (1, Answers.Answer_1),
        (2, Answers.Answer_2),
        (3, Answers.Answer_3),
        (4, Answers.Answer_4),
        (5, Answers.Answer_5),
        (6, Answers.Answer_6),
        (7, Answers.Answer_7)
    ])
    def test_get_answers_for_questions(self, driver, num, expected_answer):
        main_page = MainPage(driver)
        main_page.cookies_accept()
        main_page.click_to_questions(num)
        assert main_page.get_answers(num) == expected_answer

    @allure.title('Тестирование создания заказа')
    @allure.description('Тестирование создания заказа и перехода на главную страницу по клику на логотип Самоката')
    @pytest.mark.parametrize('button_order_locator',
                             [MainPageLocators.HEADER_ORDER_BUTTON, MainPageLocators.MAIN_BLOCK_ORDER_BUTTON])
    def test_go_to_main_page_via_scooter_logo(self, driver, button_order_locator):
        main_page = MainPage(driver)
        main_page.cookies_accept()
        main_page.create_order(button_order_locator)
        actual_result = main_page.get_main_page_via_scooter_logo()
        expected_result = 'Вопросы о важном'
        assert actual_result == expected_result

import allure
from data import *
from conftest import *
from pages.main_page import MainPage
import pytest


class TestQuestionsAnswers:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('question_number, expected_answer', [
        (0, Answers.Answer_0),
        (1, Answers.Answer_1),
        (2, Answers.Answer_2),
        (3, Answers.Answer_3),
        (4, Answers.Answer_4),
        (5, Answers.Answer_5),
        (6, Answers.Answer_6),
        (7, Answers.Answer_7)
    ])
    def test_get_answers_for_questions(self, question_number, expected_answer):
        self.driver.get(URL.main_page_url)
        main_page = MainPage(self.driver)
        main_page.get_questions_list()
        main_page.click_question(question_number)
        actual_answer = main_page.get_answer_text(question_number)
        assert actual_answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def get_questions_list(self):
        element = self.driver.find_element(*MainPageLocators.QUESTIONS_LIST)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, question_number):
        question_locator = (MainPageLocators.QUESTIONS[0], MainPageLocators.QUESTIONS[1].format(question_number))
        base_page = BasePage(self.driver)
        base_page.wait_for_element_located(question_locator)
        self.driver.find_element(*question_locator).click()

    def get_answer_text(self, answer_number):
        answer_locator = (MainPageLocators.ANSWERS[0], MainPageLocators.ANSWERS[1].format(answer_number))
        base_page = BasePage(self.driver)
        base_page.wait_for_element_located(answer_locator)
        return self.driver.find_element(*answer_locator).text

    def get_dzen_url_via_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()

    def click_order_page_via_header_open(self):
        self.driver.find_element(*MainPageLocators.HEADER_ORDER_BUTTON).click
        base_page = BasePage(self.driver)
        base_page.wait_for_element_located(MainPageLocators.CUSTOMER_FIRST_NAME)

    def click_page_via_main_block(self):
        self.driver.find_element(*MainPageLocators.MAIN_BLOCK_ORDER_BUTTON).click()
        base_page = BasePage(self.driver)
        base_page.wait_for_element_located(MainPageLocators.CUSTOMER_FIRST_NAME)



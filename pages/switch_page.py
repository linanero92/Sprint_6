import allure
import urls
from pages.base_page import BasePage
from locators.switch_page_locators import SwitchPageLocators


class SwitchPage(BasePage):

    @allure.step('Переход на главную страницу по клику на лого самоката')
    def get_main_page_via_scooter_logo(self):
        self.click_to_element(SwitchPageLocators.SCOOTER_LOGO)
        self.scroll_to_element(SwitchPageLocators.QUESTIONS_TEXT)
        return self.get_text_from_element(SwitchPageLocators.QUESTIONS_TEXT)

    @allure.step('Переход на страницу "Дзен" по клику на лого Яндекса')
    def get_dzen_via_yandex_logo(self):
        self.click_to_element(SwitchPageLocators.YANDEX_LOGO)
        self.wait_for_window_opened(2)
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        self.get_url(urls.DZEN_PAGE_URL)

    @allure.step('Поиск кнопки "Найти" на странице "Дзен"')
    def get_find_button_on_dzen(self):
        return self.get_text_from_element(SwitchPageLocators.DZEN_WINDOW_FIND_BUTTON)

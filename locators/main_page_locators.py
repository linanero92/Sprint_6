from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIES_BUTTON = [By.XPATH, '//button[contains(@class, "App_CookieButton")]']
    QUESTIONS_LIST = [By.XPATH, '//div[@class="accordion"]']
    QUESTIONS = [By.XPATH, '//div[@id="accordion__heading-{}"]']
    ANSWERS = [By.XPATH, '//div[@id="accordion__panel-{}"]']
    HEADER_ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Header_Nav")]//button[text()="Заказать"]']
    MAIN_BLOCK_ORDER_BUTTON = [By.XPATH, '/div[contains(@class, "Home_FinishButton")]//button[text()="Заказать"]']

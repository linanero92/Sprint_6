import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from helpers import Generators


class OrderPage(BasePage):

    @allure.step('Ввод данных клиента')
    @allure.step('Заполнено поле "Имя"')
    @allure.step('Заполнено поле "Фамилия"')
    @allure.step('Заполнено поле "Адрес: куда привезти заказ"')
    @allure.step('Выбрана станция метро')
    @allure.step('Заполнено поле "Телефон"')
    @allure.step('Клик по кнопке "Далее"')
    @allure.step('Заполнено поле с датой "Куда привезти заказ"')
    @allure.step('Выбран период Аренды')
    @allure.step('Выбран цвет самоката')
    @allure.step('Заполнено поле "Комментарий для курьера"')
    @allure.step('Клик по кпопкам "Заказать" и "Да"')
    @allure.step('Клик по кнопке "Посмотреть статус"')
    @allure.description('Заполнение и отправка формы с данными клиента')
    def set_order(self):
        generators = Generators()
        first_name = generators.generate_first_name()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_FIRST_NAME, first_name)
        last_name = generators.generate_last_name()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_LAST_NAME, last_name)
        address = generators.generate_address()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_ADDRESS, address)
        self.click_to_element(OrderPageLocators.METRO_STATION_FIELD)
        self.click_to_element(OrderPageLocators.DROP_DOWN_STATION_NAME)
        phone_number = generators.generate_phone_number()
        self.add_text_to_element(OrderPageLocators.CUSTOMER_PHONE, phone_number)
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        delivery_data = generators.generate_delivery_date()
        self.add_text_to_element(OrderPageLocators.DELIVERY_DATE_FIELD, delivery_data)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_SELECT)
        scooter_color = generators.generate_scooter_color()
        self.add_text_to_element(OrderPageLocators.SCOOTER_COLOR, scooter_color)
        comment = generators.generate_comment()
        self.add_text_to_element(OrderPageLocators.COMMENT, comment)
        self.click_to_element(OrderPageLocators.FORM_ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.ORDER_CONFIRM_BUTTON)
        self.click_to_element(OrderPageLocators.ORDER_STATUS_BUTTON)

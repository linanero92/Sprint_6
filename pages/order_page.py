import allure
from helpers import Generators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def cookies_acception(self):
        self.driver.find_element(*OrderPageLocators.COOKIES_BUTTON).click()

    def set_first_name(self):
        generators = Generators(self.driver)
        first_name = generators.generate_first_name()
        self.driver.find_element(*OrderPageLocators.CUSTOMER_FIRST_NAME).send_keys(first_name)

    def set_last_name(self):
        generators = Generators(self.driver)
        last_name = generators.generate_last_name()
        self.driver.find_element(*OrderPageLocators.CUSTOMER_LAST_NAME).send_keys(last_name)

    def set_address(self):
        generators = Generators(self.driver)
        address = generators.generate_address()
        self.driver.find_element(*OrderPageLocators.CUSTOMER_ADDRESS).send_keys(address)

    def set_metro_station(self):
        generators = Generators(self.driver)
        metro_station = generators.generate_metro_station()
        self.driver.find_element(*OrderPageLocators.METRO_STATION_FIELD).click()
        station_select = self.driver.find_element(*OrderPageLocators.METRO_STATION_SELECT).send_keys(metro_station)
        station_select.click()

    def set_phone_number(self):
        generators = Generators(self.driver)
        phone_number = generators.generate_phone_number()
        self.driver.find_element(*OrderPageLocators.CUSTOMER_PHONE).send_keys(phone_number)

    def next_fields_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click

    def set_delivery_data(self):
        base_page = BasePage(self.driver)
        base_page.wait_for_element_located(OrderPageLocators.DELIVERY_DATE_FIELD)
        generators = Generators(self.driver)
        delivery_data = generators.generate_delivery_date()
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_FIELD).send_keys(delivery_data)

    def set_rental_period(self):
        generators = Generators(self.driver)
        rental_period = generators.generate_rental_period()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        rental_period_select = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_SELECT).send_keys(rental_period)
        rental_period_select.click()

    def set_scooter_color(self):
        generators = Generators(self.driver)
        scooter_color = generators.generate_scooter_color()
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR).send_keys(scooter_color)

    def set_comment(self):
        generators = Generators(self.driver)
        comment = generators.generate_comment()
        self.driver.find_element(*OrderPageLocators.COMMENT).send_keys(comment)

    def click_order_and_confirm_buttons(self):
        self.driver.find_element(*OrderPageLocators.FORM_ORDER_BUTTON).click()
        base_page = BasePage(self.driver)
        base_page.wait_for_element_located(OrderPageLocators.ORDER_CONFIRM_BUTTON).click()

    def get_main_page_via_scooter_logo(self):
        self.driver.find_element(*OrderPageLocators.SCOOTER_LOGO).click()

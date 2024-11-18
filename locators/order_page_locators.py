from selenium.webdriver.common.by import By


class OrderPageLocators:

    SCOOTER_LOGO = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]']
    YANDEX_LOGO = [By.XPATH, '//a[@class="Header_LogoYandex"]']
    CUSTOMER_FIRST_NAME = [By.XPATH, '//input[contains(@class, "Input_Input", "Input_Responsible") and contains(@placeholder, "* Имя")]']
    CUSTOMER_LAST_NAME = [By.XPATH, '//input[contains(@class, "Input_Input", "Input_Responsible") and contains(@placeholder, "* Фамилия")]']
    CUSTOMER_ADDRESS = [By.XPATH, '//input[contains(@class, "Input_Input", "Input_Responsible") and contains(@placeholder, "* Адрес: куда привезти заказ")]']
    METRO_STATION_FIELD = [By.XPATH, '//div[contains(@class, "select-search__value")]//input[contains(@class, "select-search__input") and contains(@placeholder, "Станция метро")]']
    METRO_STATION_SELECT = [By.XPATH, '//div[contains(@class, "select-search has-focus")]//div[contains(@class, "select-search__select")']
    CUSTOMER_PHONE = [By.XPATH, '//input[contains(@class, "Input_Input", "Input_Responsible") and contains(@placeholder, "* Телефон: на него позвонит курьер")]']
    NEXT_BUTTON = [By.XPATH, '//div[contains(@class, "Order_NextButton")]//button[contains(@class, "Button_Button") and contains(@class, "Button_Middle") and text()="Далее"]']
    DELIVERY_DATE_FIELD = [By.XPATH, '//div[contains(@class, "react-datepicker__input-container")]//input[contains(@class, "Input_Input")]']
    RENTAL_PERIOD = [By.XPATH, '//div[contains(@class, "Dropdown-control") and @aria-haspopup="listbox"]//div[contains(@class, "Dropdown-placeholder") and text()="* Срок аренды"]']
    RENTAL_PERIOD_SELECT = [By.XPATH, '//div[contains(@class, "Dropdown-root") and contains(@class, "is-open")]//div[contains(@class, "Dropdown-option")']
    SCOOTER_COLOR = [By.XPATH, '//div[contains(@class, "Order_Checkboxes")]//label[contains(@class, "Checkbox_Label")]/input[@type="checkbox"]']
    COMMENT = [By.XPATH, '//input[contains(@class, "Input_Input", "Input_Responsible") and contains(@placeholder, "Комментарий для курьера")]']
    FORM_ORDER_BUTTON = [By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[contains(@class, "Button_Button") and not(contains(@class, "Button_Inverted")) and text()="Заказать"]']
    ORDER_CONFIRM_BUTTON = [By.XPATH, '//button[contains(@class, "Button_Button") and contains(@class, "Button_Middle") and text()="Да"]']
    ORDER_PLACED = [By.XPATH, '//div[contains(@class, "Order_ModalHeader") and starts-with(text(), "Заказ оформлен")]']

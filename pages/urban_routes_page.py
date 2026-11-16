from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Clase UrbanRoutesPage con los localizadores y métodos necesarios para las pruebas
class UrbanRoutesPage:

#   Localizadores

#   1. By.ID
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    phone_input = (By.ID, 'phone')
    phone_code_input = (By.ID, 'code')
    card_number_input = (By.ID, 'number')
    driver_message_field = (By.ID, 'comment')

#   2. By.CLASS_NAME
    phone_button = (By.CLASS_NAME, 'np-text')
    payment_method_button = (By.CLASS_NAME, 'pp-text')
    add_card_button = (By.CLASS_NAME, 'pp-plus')
    order_button = (By.CLASS_NAME, 'smart-button-wrapper')

#   3. By.XPATH
    comfort_tariff_card = (By.XPATH, '//div[contains(@class, "tariff-card")]//div[text()="Comfort"]')
    comfort_tariff_active = (By.XPATH,
                               '//div[contains(@class, "tariff-card") and contains(@class, "active")]'
                               '//div[text()="Comfort"]')
    phone_next_button = (By.XPATH, '//button[text()="Siguiente"]')
    phone_confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
    card_code_input = (By.XPATH, '//div[@class="card-code-input"]//input[@id="code"]')
    link_card_button = (By.XPATH, '//button[text()="Agregar"]')
    card_added_check = (By.XPATH, '//div[@class="pp-title" and text()="Tarjeta"]')
    blanket_tissue_switch = (By.XPATH, '//div[contains(text(), "Manta")]/..//span[contains(@class, "slider")]')
    blanket_tissue_checkbox = (By.XPATH, '//div[contains(text(), "Manta")]/..//input')
    ice_cream_plus_button = (By.XPATH, '//div[contains(text(), "Helado")]/..//div[@class="counter-plus"]')
    ice_cream_counter = (By.XPATH, '//div[contains(text(), "Helado")]/..//div[@class="counter-value"]')
    driver_info_header = (By.XPATH, '//div[contains(@class, "order-header-title")]')

#   4. By.CSS_SELECTOR
    call_taxi_button = (By.CSS_SELECTOR, 'button.button.round')
    close_payment_modal_button = (By.CSS_SELECTOR, '.payment-picker .close-button')
    order_modal_body = (By.CSS_SELECTOR, '.order-body')

#   Constructor
    def __init__(self, driver):
        self.driver = driver

#   Métodos

#   1. Métodos para Configurar la dirección.
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self,from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

#   2. Métodos para Seleccionar la tarifa Comfort.
    def select_comfort_tariff(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            self.comfort_tariff_card))
        self.driver.find_element(*self.comfort_tariff_card).click()

    def is_comfort_tariff_selected(self):
        return 'active' in self.driver.find_element(By.XPATH, '//*[text()="Comfort"]/..').get_attribute('class')

#   3. Métodos para Rellenar el número de teléfono.
    def click_phone_button(self):
        self.driver.find_element(*self.phone_button).click()

    def set_phone_number(self, phone):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            self.phone_input))
        self.driver.find_element(*self.phone_input).send_keys(phone)

    def click_phone_next(self):
        self.driver.find_element(*self.phone_next_button).click()

    def set_phone_code(self, code):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            self.phone_code_input))
        self.driver.find_element(*self.phone_code_input).send_keys(code)

    def click_phone_confirm(self):
        self.driver.find_element(*self.phone_confirm_button).click()

    def get_phone_number_value(self):
        return self.driver.find_element(*self.phone_button).text

#   4. Métodos para Agregar una tarjeta de crédito.
    def click_payment_method(self):
        self.driver.find_element(*self.payment_method_button).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.add_card_button))
        self.driver.find_element(*self.add_card_button).click()

    def set_card_number(self, card_num):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            self.card_number_input))
        self.driver.find_element(*self.card_number_input).send_keys(card_num)

    def set_card_code(self,card_code):
        card_code_elem = self.driver.find_element(*self.card_code_input)
        card_code_elem.send_keys(card_code)
        # Cambio de foco simulando TAB para habilitar el botón "Agregar"
        card_code_elem.send_keys(Keys.TAB)

    def click_link_card(self):
        self.driver.find_element(*self.link_card_button).click()

    def close_payment_modal(self):
        self.driver.find_element(*self.close_payment_modal_button).click()

    def is_card_added(self):
        return len(self.driver.find_elements(*self.card_added_check)) > 0

#   5. Métodos para Escribir un mensaje para el controlador.
    def set_driver_message(self, message):
        self.driver.find_element(*self.driver_message_field).send_keys(message)

    def get_driver_message(self):
        return self.driver.find_element(*self.driver_message_field).get_property('value')

#   6. Métodos para Pedir una manta y pañuelos.
    def toggle_blanket_and_tissues(self):
        # Esperamos a que el interruptor esté listo para hacer clic
        switch_elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.blanket_tissue_switch))
        # Desplazamos la pantalla hasta el elemento para asegurar el clic
        self.driver.execute_script("arguments[0].scrollIntoView();", switch_elem)
        switch_elem.click()

    def is_blanket_and_tissues_selected(self):
        # Esperamos a que el input tipo checkbox esté en el DOM y retorna si está marcado(.is\_selected())
        checkbox_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.blanket_tissue_checkbox))
        return checkbox_elem.is_selected()

#   7. Métodos para Pedir 2 helados.
    def add_ice_cream(self, quantity=2):
        for  _ in range(quantity):
            self.driver.find_element(*self.ice_cream_plus_button).click()
    def get_ice_cream_count(self):
        return int(self.driver.find_element(*self.ice_cream_counter).text)

#   8. Métodos para Aparece el modal para buscar un taxi.
    def click_order_taxi(self):
        self.driver.find_element(*self.order_button).click()

    def is_order_modal_displayed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            self.order_modal_body))
        return self.driver.find_element(*self.order_modal_body).is_displayed()

#   9. Métodos para Esperar a que aparezca la información del conductor en el modal.
    def wait_for_driver_info(self, timeout=60):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(
            self.driver_info_header))
        return self.driver.find_element(*self.driver_info_header).is_displayed()

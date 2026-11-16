from data import data
from utils.retrieve_code import retrieve_phone_code
from selenium import webdriver
from pages.urban_routes_page import UrbanRoutesPage

#   Clase TestUrbanRoutes con las pruebas
class TestUrbanRoutes:

    driver = None

#   Método para preparar un navegador limpio y fresco para cada prueba ya con Urban Routes.
    def setup_method(self):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

#   Método para cerrar navegador creado por cada prueba
    def teardown_method(self):
            self.driver.quit()

    #   1. Configurar la dirección.
    def test_set_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

#   2. Seleccionar la tarifa Comfort.
    def test_select_comfort_tariff(self):
       self.routes_page.set_route(data.address_from, data.address_to)
       self.routes_page.click_call_taxi_button()
       self.routes_page.select_comfort_tariff()
       assert self.routes_page.is_comfort_tariff_selected()

#   3. Rellenar el número de teléfono.
    def test_fill_phone_number(self):
       self.routes_page.set_route(data.address_from, data.address_to)
       self.routes_page.click_call_taxi_button()
       self.routes_page.select_comfort_tariff()
       self.routes_page.click_phone_button()
       self.routes_page.set_phone_number(data.phone_number)
       self.routes_page.click_phone_next()
       code = retrieve_phone_code(self.driver)
       self.routes_page.set_phone_code(code)
       self.routes_page.click_phone_confirm()
       assert self.routes_page.get_phone_number_value() == data.phone_number

#   4. Agregar una tarjeta de crédito.
    def test_add_credit_card(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_tariff()
        self.routes_page.click_payment_method()
        self.routes_page.click_add_card()
        self.routes_page.set_card_number(data.card_number)
        self.routes_page.set_card_code(data.card_code)
        self.routes_page.click_link_card()
        self.routes_page.close_payment_modal()
        assert self.routes_page.is_card_added()

#   5. Escribir un mensaje para el controlador.
    def test_write_driver_comment(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_tariff()
        self.routes_page.set_driver_message(data.message_for_driver)
        assert self.routes_page.get_driver_message() == data.message_for_driver

#   6. Pedir una manta y pañuelos.
    def test_order_blanket_and_tissues(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_tariff()
        self.routes_page.toggle_blanket_and_tissues()
        assert self.routes_page.is_blanket_and_tissues_selected()

#   7. Pedir 2 helados.
    def test_order_ice_cream(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_tariff()
        self.routes_page.add_ice_cream(2)
        assert self.routes_page.get_ice_cream_count() == 2

#   8. Aparece el modal para buscar un taxi.
    def test_taxi_modal_appears(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_tariff()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_phone_confirm()
        self.routes_page.set_driver_message(data.message_for_driver)
        self.routes_page.toggle_blanket_and_tissues()
        self.routes_page.add_ice_cream(2)
        self.routes_page.click_order_taxi()
        assert self.routes_page.is_order_modal_displayed()

#   9. Esperar a que aparezca la información del conductor en el modal.
    def test_driver_info_appears(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_call_taxi_button()
        self.routes_page.select_comfort_tariff()
        self.routes_page.click_phone_button()
        self.routes_page.set_phone_number(data.phone_number)
        self.routes_page.click_phone_next()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_phone_code(code)
        self.routes_page.click_phone_confirm()
        self.routes_page.set_driver_message(data.message_for_driver)
        self.routes_page.toggle_blanket_and_tissues()
        self.routes_page.add_ice_cream(2)
        self.routes_page.click_order_taxi()
        assert self.routes_page.wait_for_driver_info(timeout=60)


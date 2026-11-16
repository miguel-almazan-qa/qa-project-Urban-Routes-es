# Proyecto Urban Routes - Pruebas Automatizadas de UI (Sprint 9)

Este repositorio contiene la suite completa de pruebas automatizadas de interfaz de usuario para la aplicación web **Urban Routes**. El proyecto está desarrollado en Python utilizando **Selenium WebDriver** y **PyTest**, aplicando una arquitectura modular del patrón de diseño **Page Object Model (POM)** organizada en paquetes.

---

## 🛠️ Tecnologías y Herramientas

* **Lenguaje de Programación:** Python 3.x
* **Herramienta de Automatización:** Selenium WebDriver 4
* **Framework de Pruebas:** PyTest
* **Patrón de Diseño:** Page Object Model (POM) con arquitectura modular de paquetes
* **IDE Recomendado:** PyCharm
* **Navegador:** Google Chrome

---

## 📁 Estructura del Proyecto

```text
qa-project-Urban-Routes-es/
├── data/
│   ├── __init__.py
│   └── data.py                # Variables globales y datos de prueba (URLs, direcciones, tarjeta, etc.).
├── pages/
│   ├── __init__.py
│   └── urban_routes_page.py   # Clase Page Object (UrbanRoutesPage) con localizadores y métodos de acción.
├── tests/
│   └── test_urban_routes.py   # Clase de pruebas (TestUrbanRoutes) con los 9 escenarios de prueba independientes.
├── utils/
│   ├── __init__.py
│   └── retrieve_code.py       # Función auxiliar (retrieve_phone_code) para extraer el código SMS de los logs de red.
└── README.md                  # Documentación del proyecto e instrucciones de ejecución.
```

### Componentes Clave

1. **`pages/urban_routes_page.py` (`UrbanRoutesPage`)**:
   Encapsula la estructura y acciones de la página. Implementa los 4 tipos de localizadores requeridos (`By.ID`, `By.CLASS_NAME`, `By.XPATH` y `By.CSS_SELECTOR`).
2. **`utils/retrieve_code.py` (`retrieve_phone_code`)**:
   Función auxiliar encargada de interceptar los registros de red (*performance logs*) de Chrome para obtener dinámicamente el código SMS de confirmación.
3. **`tests/test_urban_routes.py` (`TestUrbanRoutes`)**:
   Contiene los 9 escenarios de prueba autónomos e independientes. Cada prueba utiliza los hooks `setup_method()` y `teardown_method()` para garantizar una sesión de navegador limpia.
4. **`data/data.py`**:
   Centraliza todos los datos estáticos requeridos para la ejecución de los tests.

---

## 🧪 Escenarios de Prueba (9 Tests)

1. `test_set_route`: Configura la dirección de origen y destino en el formulario inicial.
2. `test_select_comfort_tariff`: Selecciona la tarifa "Comfort" y valida su activación.
3. `test_fill_phone_number`: Ingresa el número telefónico, intercepta el código SMS mediante `retrieve_phone_code` y confirma el número.
4. `test_add_credit_card`: Enlaza una tarjeta de crédito/débito ingresando el número y código CVV (manejando el cambio de foco con `Keys.TAB` para habilitar el botón "Agregar").
5. `test_write_driver_comment`: Escribe un mensaje personalizado para el conductor.
6. `test_order_blanket_and_tissues`: Activa el interruptor para pedir manta y pañuelos adicionales (utilizando desplazamiento con `scrollIntoView` de JavaScript).
7. `test_order_ice_cream`: Selecciona 2 helados utilizando el contador de la interfaz.
8. `test_taxi_modal_appears`: Completa el flujo de pedido y confirma que aparece el modal de búsqueda de taxi.
9. `test_driver_info_appears`: Espera hasta 60 segundos a que la aplicación asignará un conductor y se muestre su información en pantalla.

---

## 🚀 Instrucciones de Instalación y Ejecución

### 1. Requisitos Previos
Asegúrate de tener instalado Python 3 y las dependencias necesarias:
```bash
pip install selenium pytest
```

### 2. Configuración del Servidor
Abre el archivo `data/data.py` y actualiza la variable `urban_routes_url` con la URL activa de tu servidor de Urban Routes.

### 3. Ejecución de las Pruebas con PyTest

* **Ejecutar toda la suite de pruebas:**
  ```bash
  pytest
  ```
  o especificando la ruta del módulo de pruebas:
  ```bash
  pytest tests/test_urban_routes.py
  ```

* **Ejecutar una prueba específica:**
  ```bash
  pytest tests/test_urban_routes.py::TestUrbanRoutes::test_select_comfort_tariff
  ```

* **Ejecutar en modo detallado (verbose):**
  ```bash
  pytest -v tests/test_urban_routes.py
  ```

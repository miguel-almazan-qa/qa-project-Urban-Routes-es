# Proyecto Urban Routes - Pruebas Automatizadas de UI (Sprint 9)

Este repositorio contiene una suite completa de pruebas automatizadas de interfaz de usuario para la aplicación web **Urban Routes**. El proyecto está desarrollado en Python utilizando **Selenium WebDriver** y **PyTest**, implementando el patrón de diseño **Page Object Model (POM)**.

\---

## 🛠️ Tecnologías y Herramientas

* **Lenguaje de Programación:** Python 3.x
* **Herramienta de Automatización:** Selenium WebDriver 4
* **Framework de Pruebas:** PyTest
* **Patrón de Diseño:** Page Object Model (POM)
* **IDE Recomendado:** PyCharm
* **Navegador:** Google Chrome

\---

## 📁 Estructura del Proyecto

```text
.
├── data.py         # Contiene las variables globales y datos de prueba (URL, direcciones, teléfono, tarjeta, mensaje).
├── main.py         # Contiene la clase Page Object (UrbanRoutesPage), la función auxiliar retrieve\_phone\_code y los 9 tests (TestUrbanRoutes).
└── README.md       # Documentación del proyecto e instrucciones de ejecución.
```

### Componentes Clave en `main.py`

1. **`UrbanRoutesPage`**: Clase que encapsula la estructura de la página, definiendo los localizadores e interactuando con los elementos de la interfaz.

   * **Tipos de localizadores utilizados**: `By.ID`, `By.CLASS\_NAME`, `By.XPATH` y `By.CSS\_SELECTOR`.
2. **`retrieve\_phone\_code(driver)`**: Función auxiliar que intercepta los registros de rendimiento de red (*performance logs*) de Chrome para extraer el código SMS de confirmación.
3. **`TestUrbanRoutes`**: Clase de pruebas que ejecuta los 9 escenarios de forma autónoma e independiente mediante `setup\_method()` y `teardown\_method()`.

\---

## 🧪 Escenarios de Prueba (9 Tests)

1. `test\_set\_route`: Configura la dirección de origen y destino en el formulario inicial.
2. `test\_select\_comfort\_tariff`: Selecciona la tarifa "Comfort" y valida su activación.
3. `test\_fill\_phone\_number`: Ingresa el número telefónico, intercepta el código SMS (con ayuda de la función auxiliar retrieve\_phone\_code) y confirma el número.
4. `test\_add\_credit\_card`: Enlaza una tarjeta de crédito ingresando el número y código CVV (se simula el cambio de foco con `Keys.TAB` para habilitar el botón "Agregar"). 
5. `test\_write\_driver\_comment`: Escribe un mensaje personalizado para el conductor.
6. `test\_order\_blanket\_and\_tissues`: Activa el interruptor para pedir manta y pañuelos adicionales.
7. `test\_order\_ice\_cream`: Selecciona 2 helados utilizando el contador de la interfaz.
8. `test\_taxi\_modal\_appears`: Completa el flujo de pedido y confirma que aparece el modal de búsqueda de taxi.
9. `test\_driver\_info\_appears`: Espera hasta 60 segundos a que la aplicación asignará un conductor y se muestre su información en pantalla.

\---

## 🚀 Instrucciones de Instalación y Ejecución

### 1\. Requisitos Previos

Asegúrate de tener instalado Python 3 y las dependencias necesarias:

```bash
pip install selenium pytest
```

### 2\. Configuración del Servidor

Abre el archivo `data.py` y actualiza la variable `urban\_routes\_url` con la URL activa de tu servidor de Urban Routes.

### 3\. Ejecución de las Pruebas

* **Ejecutar toda la suite de pruebas:**

```bash
  pytest main.py
  ```

* **Ejecutar una prueba específica:**

```bash
  pytest main.py::TestUrbanRoutes::test\_select\_comfort\_tariff
  ```

* **Ejecutar en modo detallado (verbose):**

```bash
  pytest -v main.py
  ```


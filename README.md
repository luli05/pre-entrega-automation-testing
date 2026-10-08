# Pre-Entrega Automation Testing

## Descripción

Proyecto de automatización de pruebas web realizado utilizando
Selenium WebDriver, Python y Pytest.

El sitio utilizado para las pruebas es SauceDemo.

## Tecnologías

- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Git
- GitHub

## Casos de prueba

### Login

- Ingreso con usuario válido.
- Validación de URL.
- Validación del título Products.

### Inventario

- Validación del título.
- Validación de productos.
- Obtención del nombre y precio del primer producto.
- Validación del menú.
- Validación del filtro.

### Carrito

- Agregar primer producto.
- Validar contador.
- Acceder al carrito.
- Validar producto agregado.

## Instalación

Crear entorno virtual:

python -m venv venv

Activar entorno:

.\venv\Scripts\Activate.ps1

Instalar dependencias:

pip install -r requirements.txt

## Ejecución

pytest -v

## Reporte HTML

pytest tests/test_saucedemo.py -v --html=reports/reporte.html

## Estructura
pre-entrega-automation-testing/

.gitignore          📄

reports/            📁

tests/              📁

utils/              📁

venv/               📁

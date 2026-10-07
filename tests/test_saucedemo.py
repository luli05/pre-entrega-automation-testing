import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import esperar_elemento

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


#TEST LOGIN
def test_login_exitoso(driver):

    driver.get("https://www.saucedemo.com/")

    usuario = esperar_elemento(
        driver,
        (By.ID, "user-name")
    )
    usuario.send_keys("standard_user")

    password = esperar_elemento(
        driver,
        (By.ID, "password")
    )
    password.send_keys("secret_sauce")

    boton_login = esperar_elemento(
        driver,
        (By.ID, "login-button")
    )
    boton_login.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    assert "/inventory.html" in driver.current_url

    titulo = esperar_elemento(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert titulo.text == "Products"




#Test de navegación/inventario

def test_inventario(driver):

    driver.get("https://www.saucedemo.com/")

    esperar_elemento(
        driver,
        (By.ID, "user-name")
    ).send_keys("standard_user")

    esperar_elemento(
        driver,
        (By.ID, "password")
    ).send_keys("secret_sauce")

    esperar_elemento(
        driver,
        (By.ID, "login-button")
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    # Validar título
    titulo = esperar_elemento(
        driver,
        (By.CLASS_NAME, "title")
    )

    assert titulo.text == "Products"

    # Validar productos
    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0

    # Primer producto
    primer_producto = productos[0]

    nombre = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    precio = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    print(f"Primer producto: {nombre}")
    print(f"Precio: {precio}")

    assert nombre != ""
    assert precio != ""

    # Validar filtro
    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert filtro.is_displayed()

    # Validar menú
    menu = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    )

    assert menu.is_displayed()


#TEST CARRITO

def test_agregar_producto_al_carrito(driver):

    driver.get("https://www.saucedemo.com/")

    esperar_elemento(
        driver,
        (By.ID, "user-name")
    ).send_keys("standard_user")

    esperar_elemento(
        driver,
        (By.ID, "password")
    ).send_keys("secret_sauce")

    esperar_elemento(
        driver,
        (By.ID, "login-button")
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    # Buscar el primer producto
    primer_producto = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )[0]

    nombre_producto = primer_producto.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    # Agregar al carrito
    boton_agregar = primer_producto.find_element(
        By.TAG_NAME,
        "button"
    )

    boton_agregar.click()

    # Validar contador
    contador = esperar_elemento(
        driver,
        (By.CLASS_NAME, "shopping_cart_badge")
    )

    assert contador.text == "1"

    # Ir al carrito
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/cart.html")
    )

    # Verificar producto
    producto_carrito = esperar_elemento(
        driver,
        (By.CLASS_NAME, "inventory_item_name")
    )

    assert producto_carrito.text == nombre_producto



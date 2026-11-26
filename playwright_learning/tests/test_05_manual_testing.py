
# ============================================================
# TEST 05 - AUTOMATIZACION + PRUEBAS MANUALES
# Proyecto: QA Automation con Playwright y Pytest
# Web: https://www.saucedemo.com/
# Arquitectura: Page Object Model (POM)
# ============================================================

from pages.pagina_login import PaginaLogin
from pages.pagina_productos import PaginaProductos
from pages.pagina_carrito import PaginaCarrito
from pages.detalle_producto import DetalleProducto


def test_manual_testing(page):

    # PASO 1: LOGIN
    login = PaginaLogin(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    # PASO 2: COMPROBAR PAGINA DE PRODUCTOS
    products = PaginaProductos(page)
    products.verify_products_page_is_visible()

    # PASO 3: AÑADIR MOCHILA AL CARRITO
    products.add_backpack_to_cart()
    products.verify_cart_count(1)

    # PASO 4: ABRIR CARRITO
    products.open_cart()

    cart = PaginaCarrito(page)
    cart.verify_cart_is_visible()
    cart.verify_product_count(1)
    cart.verify_product_is_visible("Sauce Labs Backpack")

    # PASO 5: ABRIR DETALLE DEL PRODUCTO
    cart.open_backpack_details()

    product_details = DetalleProducto(page)
    product_details.verify_back_button_visible()

    # PASO 6: VOLVER A PRODUCTOS
    product_details.back_to_products()
    products.verify_products_page_is_visible()

    # PASO 7: VOLVER AL CARRITO
    products.open_cart()

    # PASO 8: ELIMINAR MOCHILA
    cart.remove_backpack_from_cart()

    # PASO 9: COMPROBAR CARRITO VACIO
    cart.verify_cart_is_empty()
    products.verify_cart_count(0)

    # PASO 10: PREPARAR EXPLORACION MANUAL
    print("\n======================================")
    print("FASE AUTOMATIZADA COMPLETADA")
    print("NAVEGADOR PREPARADO PARA EXPLORACION")
    print("======================================")

    # Descomentar para pausar la ejecución y explorar manualmente:
    # page.pause()
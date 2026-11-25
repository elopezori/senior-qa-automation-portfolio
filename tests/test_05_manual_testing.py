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
from common.helpers import pausa


def test_manual_testing(page):

    # PASO 1: Crear objeto PaginaLogin
    login = PaginaLogin(page)

    # PASO 2: Abrir SauceDemo y realizar login
    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    # PASO 3: Crear objeto PaginaProductos
    products = PaginaProductos(page)

    # PASO 4: Añadir mochila al carrito
    products.add_backpack_to_cart()

    # PASO 5: Comprobar contador del carrito
    assert products.get_cart_count() == 1

    pausa(page, "Mochila añadida correctamente")

    # PASO 6: Entrar en el carrito
    products.open_cart()

    # PASO 7: Crear objeto PaginaCarrito
    cart = PaginaCarrito(page)

    # PASO 8: Comprobar producto en el carrito
    assert cart.get_product_count() == 1

    assert cart.get_product_name() == "Sauce Labs Backpack"

    pausa(page, "Producto comprobado en el carrito")

    # PASO 9: Volver a la ficha del producto
    cart.open_backpack_details()

    # PASO 10: Crear objeto DetalleProducto
    product_details = DetalleProducto(page)

    assert product_details.is_back_button_visible()

    # PASO 11: Volver a todos los productos
    product_details.back_to_products()

    # PASO 12: Volver a entrar en el carrito
    products.open_cart()

    # PASO 13: Eliminar mochila del carrito
    cart.remove_backpack_from_cart()

    # PASO 14: Comprobar que el carrito está vacío
    assert cart.get_product_count() == 0

    assert products.get_cart_count() == 0

    pausa(page, "Mochila eliminada del carrito")

    # PASO 15: Comienza la fase manual
    print("\n======================================")
    print("FASE AUTOMATIZADA COMPLETADA")
    print("AHORA COMIENZA LA PRUEBA MANUAL")
    print("======================================")

    print("\nNAVEGADOR PREPARADO PARA INTERACCION MANUAL")

    pausa(page, "Preparado para pruebas manuales")

    # page.pause()


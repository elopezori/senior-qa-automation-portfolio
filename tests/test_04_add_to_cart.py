# ============================================================
# TEST 04 - AÑADIR PRODUCTO AL CARRITO
# Proyecto: QA Automation con Playwright y Pytest
# Web: https://www.saucedemo.com/
# Arquitectura: Page Object Model (POM)
# ============================================================

from pages.pagina_login import PaginaLogin
from pages.pagina_productos import PaginaProductos
from pages.pagina_carrito import PaginaCarrito
from common.helpers import pausa


def test_add_product_to_cart(page):

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

    # PASO 5: Comprobar que el carrito indica 1 producto
    assert products.get_cart_count() == 1

    pausa(page, "Carrito actualizado: 1 producto")

    # PASO 6: Entrar en el carrito
    products.open_cart()

    # PASO 7: Crear objeto PaginaCarrito
    cart = PaginaCarrito(page)

    # PASO 8: Comprobar que estamos en el carrito
    assert "cart.html" in page.url

    pausa(page, "Página del carrito abierta")

    # PASO 9: Comprobar que hay un producto
    assert cart.get_product_count() == 1

    # PASO 10: Comprobar que es la mochila
    assert cart.get_product_name() == "Sauce Labs Backpack"

    pausa(page, "Producto encontrado en el carrito")

    # PASO 11: Resultado final
    print("\nTEST CORRECTO: PRODUCTO AÑADIDO AL CARRITO")

    pausa(page, "Fin del test")

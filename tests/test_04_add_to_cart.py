
# ============================================================
# TEST 04 - AÑADIR PRODUCTO AL CARRITO
# Proyecto: QA Automation con Playwright y Pytest
# Web: https://www.saucedemo.com/
# Arquitectura: Page Object Model (POM)
# ============================================================

from pages.pagina_login import PaginaLogin
from pages.pagina_productos import PaginaProductos
from pages.pagina_carrito import PaginaCarrito


def test_add_product_to_cart(page):

    # ARRANGE: preparar la sesión
    login = PaginaLogin(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = PaginaProductos(page)
    products.verify_products_page_is_visible()

    # ACT: añadir producto al carrito
    products.add_backpack_to_cart()

    # ASSERT: comprobar contador del carrito
    products.verify_cart_count(1)

    # ACT: abrir carrito
    products.open_cart()

    cart = PaginaCarrito(page)

    # ASSERT: comprobar contenido del carrito
    cart.verify_cart_is_visible()
    cart.verify_product_count(1)
    cart.verify_product_is_visible("Sauce Labs Backpack")
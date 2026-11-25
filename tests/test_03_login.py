# ============================================================
# TEST 03 - LOGIN
# Proyecto: QA Automation con Playwright y Pytest
# Web: https://www.saucedemo.com/
# Arquitectura: Page Object Model (POM)
# ============================================================

from pages.pagina_login import PaginaLogin
from common.helpers import pausa


def test_saucedemo_login(page):

    # PASO 1: Crear objeto de la página Login
    login = PaginaLogin(page)

    # PASO 2: Abrir SauceDemo
    login.open()

    # PASO 3: Realizar login
    login.login(
        "standard_user",
        "secret_sauce"
    )

    # PASO 4: Comprobar acceso correcto
    assert "inventory.html" in login.get_url()
    assert login.is_products_page_visible()

    print("\nTEST CORRECTO: LOGIN REALIZADO")

    # PASO 5: Mantener catálogo visible
    pausa(page, "Fin del test")

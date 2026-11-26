# ============================================================
# TEST 03 - LOGIN
# Proyecto: QA Automation con Playwright y Pytest
# Web: https://www.saucedemo.com/
# Arquitectura: Page Object Model (POM)
# ============================================================


from playwright.sync_api import expect
from pages.pagina_login import PaginaLogin


def test_saucedemo_login(page):

    # Arrange: preparar la página
    login = PaginaLogin(page)
    login.open()

    # Act: realizar login
    login.login("standard_user", "secret_sauce")

    # Assert: comprobar acceso correcto
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    login.verify_products_page()
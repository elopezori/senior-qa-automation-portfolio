# ============================================================
# TEST 02 - GOOGLE A SAUCEDEMO
# Proyecto: QA Automation con Playwright y Pytest
# Webs: https://www.google.com/ y https://www.saucedemo.com/
# ============================================================

from pages.google_page import PaginaGoogle
from pages.pagina_login import PaginaLogin
from common.helpers import pausa


def test_google_to_saucedemo(page):

    # PASO 1: Crear objeto PaginaGoogle
    google = PaginaGoogle(page)

    # PASO 2: Abrir Google
    google.open()

    # PASO 3: Rechazar consentimiento si aparece
    google.reject_cookies()

    # PASO 4: Comprobar que estamos en Google
    assert "google.com" in google.get_url()
    pausa(page, "Google comprobado")

    # PASO 5: Crear objeto PaginaLogin
    login = PaginaLogin(page)

    # PASO 6: Navegar a SauceDemo
    login.open()

    # PASO 7: Comprobar que estamos en SauceDemo
    assert "saucedemo.com" in login.get_url()

    # PASO 8: Comprobar que aparece el formulario
    assert login.is_login_form_visible()

    print("\nTEST CORRECTO: hemos llegado a SauceDemo")

    # PASO 9: Mantener la página visible
    pausa(page, "Fin del test")

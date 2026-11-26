
# ============================================================
# TEST 02 - GOOGLE A SAUCEDEMO
# Proyecto: QA Automation con Playwright y Pytest
# Webs: https://www.google.com/ y https://www.saucedemo.com/
# ============================================================

import re

from playwright.sync_api import expect

from pages.google_page import PaginaGoogle
from pages.pagina_login import PaginaLogin


def test_google_to_saucedemo(page):

    # PASO 1: Crear objeto PaginaGoogle
    google = PaginaGoogle(page)

    # PASO 2: Abrir Google
    google.open()

    # PASO 3: Rechazar consentimiento si aparece
    google.reject_cookies()

    # PASO 4: Comprobar que estamos en Google
    expect(page).to_have_url(re.compile(r"google\.com"))

    # PASO 5: Crear objeto PaginaLogin
    login = PaginaLogin(page)

    # PASO 6: Navegar a SauceDemo
    login.open()

    # PASO 7: Comprobar que estamos en SauceDemo
    expect(page).to_have_url(re.compile(r"saucedemo\.com"))

    # PASO 8: Comprobar que aparece el formulario
    assert login.is_login_form_visible()

    print("\nTEST CORRECTO: hemos llegado a SauceDemo")
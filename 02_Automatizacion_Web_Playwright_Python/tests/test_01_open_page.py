# ============================================================
# TEST 01 - GOOGLE PAGINA PRINCIPAL
# Proyecto: QA Automation con Playwright y Pytest
# Web: https://www.google.com/
# ============================================================

from pages.google_page import PaginaGoogle


def test_open_page(page):

    # PASO 1: Crear objeto PaginaGoogle
    google = PaginaGoogle(page)

    # PASO 2: Abrir Google
    google.open()

    # PASO 3: Gestionar cookies
    google.reject_cookies()

    # PASO 4: Comprobar página
    assert "google.com" in google.get_url()

    print("\nTEST CORRECTO: GOOGLE ABIERTO")



import logging

from playwright.sync_api import Page, expect


class PaginaGoogle:

    URL = "https://www.google.com"

    def __init__(self, page: Page):
        self.page = page

        # SELECTORES
        self.search_box = page.locator('textarea[name="q"]')
        self.reject_cookies_button = page.get_by_role(
            "button",
            name="Rechazar todo"
        )

    # ACCIONES

    def open(self):
        self.page.goto(self.URL)
        logging.info("Google abierto")

    def reject_cookies(self):
        try:
            self.reject_cookies_button.click(timeout=3000)
            logging.info("Cookies rechazadas")
        except Exception:
            logging.info(
                "No se ha mostrado el botón de consentimiento"
            )

    def search(self, text):
        self.search_box.fill(text)
        self.search_box.press("Enter")
        logging.info("Búsqueda realizada: %s", text)

    # COMPROBACIONES

    def get_url(self):
        return self.page.url

    def is_search_box_visible(self):
        return self.search_box.is_visible()

    def verify_search_box_visible(self):
        expect(self.search_box).to_be_visible()
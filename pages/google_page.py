from common.helpers import pausa


class PaginaGoogle:

    def __init__(self, page):
        self.page = page

        # SELECTORES
        self.search_box = page.locator('textarea[name="q"]')
        self.reject_cookies_button = page.get_by_role(
            "button",
            name="Rechazar todo"
        )

    # ACCIONES

    def open(self):
        self.page.goto("https://www.google.com")
        pausa(self.page, "Google abierto")

    def reject_cookies(self):
        try:
            self.reject_cookies_button.click(timeout=3000)
            pausa(self.page, "Cookies rechazadas")
        except Exception:
            print("No se ha mostrado el botón de consentimiento")

    def search(self, text):
        self.search_box.fill(text)
        self.search_box.press("Enter")
        pausa(self.page, "Búsqueda realizada")

    # COMPROBACIONES

    def get_url(self):
        return self.page.url

    def is_search_box_visible(self):
        return self.search_box.is_visible()
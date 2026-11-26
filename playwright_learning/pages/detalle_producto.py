
from playwright.sync_api import Page, expect


class DetalleProducto:

    def __init__(self, page: Page):
        self.page = page

        # SELECTORES
        self.back_to_products_button = page.locator(
            '[data-test="back-to-products"]'
        )

    # ACCIONES

    def back_to_products(self):
        self.back_to_products_button.click()

    # COMPROBACIONES

    def verify_back_button_visible(self):
        expect(self.back_to_products_button).to_be_visible()
from common.helpers import pausa


class DetalleProducto:

    def __init__(self, page):
        self.page = page

        # SELECTORES
        self.back_to_products_button = page.locator(
            '[data-test="back-to-products"]'
        )

    # ACCIONES

    def back_to_products(self):
        self.back_to_products_button.click()
        pausa(self.page, "Volvemos a todos los productos")

    # COMPROBACIONES

    def is_back_button_visible(self):
        return self.back_to_products_button.is_visible()


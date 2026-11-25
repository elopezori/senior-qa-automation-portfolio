
from common.helpers import pausa


class PaginaCheckout:

    def __init__(self, page):
        self.page = page

        # ==================================
        # SELECTORES DEL FORMULARIO
        # ==================================

        self.first_name = page.locator(
            '[data-test="firstName"]'
        )
        self.last_name = page.locator(
            '[data-test="lastName"]'
        )
        self.postal_code = page.locator(
            '[data-test="postalCode"]'
        )

        self.continue_button = page.locator(
            '[data-test="continue"]'
        )
        self.cancel_button = page.locator(
            '[data-test="cancel"]'
        )
        self.error_message = page.locator(
            '[data-test="error"]'
        )

        # ==================================
        # SELECTORES DEL RESUMEN
        # ==================================

        self.summary_items = page.locator(".cart_item")
        self.summary_subtotal = page.locator(
            ".summary_subtotal_label"
        )
        self.summary_tax = page.locator(
            ".summary_tax_label"
        )
        self.summary_total = page.locator(
            ".summary_total_label"
        )

        self.finish_button = page.locator(
            '[data-test="finish"]'
        )

        # ==================================
        # SELECTORES DE CONFIRMACION
        # ==================================

        self.complete_header = page.locator(
            ".complete-header"
        )
        self.complete_text = page.locator(
            ".complete-text"
        )
        self.back_home_button = page.locator(
            '[data-test="back-to-products"]'
        )

    # ==================================
    # ACCIONES DEL FORMULARIO
    # ==================================

    def enter_first_name(self, first_name):
        self.first_name.fill(first_name)
        pausa(self.page, "Nombre introducido")

    def enter_last_name(self, last_name):
        self.last_name.fill(last_name)
        pausa(self.page, "Apellidos introducidos")

    def enter_postal_code(self, postal_code):
        self.postal_code.fill(postal_code)
        pausa(self.page, "Código postal introducido")

    def fill_checkout_information(
        self, first_name, last_name, postal_code
    ):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)

    def continue_checkout(self):
        self.continue_button.click()
        pausa(self.page, "Continuamos con la compra")

    def cancel_checkout(self):
        self.cancel_button.click()
        pausa(self.page, "Compra cancelada")

    # ==================================
    # ACCIONES DEL RESUMEN
    # ==================================

    def finish_order(self):
        self.finish_button.click()
        pausa(self.page, "Pedido finalizado")

    # ==================================
    # VOLVER A PRODUCTOS
    # ==================================

    def back_to_products(self):
        self.back_home_button.click()
        pausa(self.page, "Volvemos a los productos")

    # ==================================
    # COMPROBACIONES
    # ==================================

    def get_error_message(self):
        return self.error_message.inner_text()

    def get_summary_product_count(self):
        return self.summary_items.count()

    def get_subtotal(self):
        return self.summary_subtotal.inner_text()

    def get_tax(self):
        return self.summary_tax.inner_text()

    def get_total(self):
        return self.summary_total.inner_text()

    def get_confirmation_message(self):
        return self.complete_header.inner_text()

    def is_order_completed(self):
        return self.complete_header.is_visible()


from playwright.sync_api import Page, expect


class PaginaCheckout:

    def __init__(self, page: Page):
        self.page = page

        # FORMULARIO
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')

        self.continue_button = page.locator('[data-test="continue"]')
        self.cancel_button = page.locator('[data-test="cancel"]')
        self.error_message = page.locator('[data-test="error"]')

        # RESUMEN
        self.summary_items = page.locator(".cart_item")
        self.summary_subtotal = page.locator(".summary_subtotal_label")
        self.summary_tax = page.locator(".summary_tax_label")
        self.summary_total = page.locator(".summary_total_label")
        self.finish_button = page.locator('[data-test="finish"]')

        # CONFIRMACIÓN
        self.complete_header = page.locator(".complete-header")
        self.complete_text = page.locator(".complete-text")
        self.back_home_button = page.locator(
            '[data-test="back-to-products"]'
        )

    # FORMULARIO

    def fill_checkout_information(
        self, first_name, last_name, postal_code
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def cancel_checkout(self):
        self.cancel_button.click()

    # RESUMEN

    def finish_order(self):
        self.finish_button.click()

    def get_summary_product_count(self):
        return self.summary_items.count()

    def get_subtotal(self):
        return self.summary_subtotal.inner_text()

    def get_tax(self):
        return self.summary_tax.inner_text()

    def get_total(self):
        return self.summary_total.inner_text()

    # CONFIRMACIÓN

    def back_to_products(self):
        self.back_home_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()

    def get_confirmation_message(self):
        return self.complete_header.inner_text()

    # VALIDACIONES

    def verify_checkout_error(self):
        expect(self.error_message).to_be_visible()

    def verify_order_completed(self):
        expect(self.complete_header).to_have_text(
            "Thank you for your order!"
        )

    def verify_summary_is_visible(self):
        expect(self.summary_items.first).to_be_visible()

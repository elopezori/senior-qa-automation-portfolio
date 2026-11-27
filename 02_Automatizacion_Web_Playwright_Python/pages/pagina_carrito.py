
from playwright.sync_api import Page, expect


class PaginaCarrito:

    def __init__(self, page: Page):
        self.page = page

        # SELECTORES GENERALES
        self.page_title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.product_names = page.locator(
            ".cart_item .inventory_item_name"
        )
        self.product_prices = page.locator(
            ".cart_item .inventory_item_price"
        )
        self.product_quantities = page.locator(".cart_quantity")

        # BOTONES
        self.continue_shopping_button = page.locator(
            '[data-test="continue-shopping"]'
        )
        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )

    # ACCIONES

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()

    def remove_product(self, product_id):
        remove_button = self.page.locator(
            f'[data-test="remove-{product_id}"]'
        )
        remove_button.click()

    def remove_backpack_from_cart(self):
        self.remove_product("sauce-labs-backpack")

    def open_backpack_details(self):
        self.page.locator(
            '[data-test="item-4-title-link"]'
        ).click()

    # CONSULTAS

    def get_product_count(self):
        return self.cart_items.count()

    def get_product_names(self):
        return self.product_names.all_inner_texts()

    def get_product_name(self):
        return self.product_names.first.inner_text()

    def get_product_prices(self):
        return self.product_prices.all_inner_texts()

    def get_page_title(self):
        return self.page_title.inner_text()

    # VALIDACIONES

    def verify_cart_is_visible(self):
        expect(self.page_title).to_have_text("Your Cart")

    def verify_product_count(self, expected_count):
        expect(self.cart_items).to_have_count(expected_count)

    def verify_product_is_visible(self, product_name):
        expect(
            self.product_names.filter(has_text=product_name)
        ).to_be_visible()

    def verify_cart_is_empty(self):
        expect(self.cart_items).to_have_count(0)
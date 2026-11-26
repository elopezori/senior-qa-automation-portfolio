
from playwright.sync_api import Page, expect


class PaginaProductos:

    def __init__(self, page: Page):
        self.page = page

        # SELECTORES GENERALES
        self.page_title = page.locator(".title")
        self.product_list = page.locator(".inventory_list")
        self.product_items = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.product_prices = page.locator(".inventory_item_price")

        # SELECTOR DE ORDENACION
        self.sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

        # SELECTORES DEL CARRITO
        self.shopping_cart = page.locator(".shopping_cart_link")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

    # ACCIONES GENERALES

    def wait_for_products(self):
        expect(self.product_list).to_be_visible()

    def open_cart(self):
        self.shopping_cart.click()

    def select_sort_option(self, option):
        self.sort_dropdown.select_option(option)

    # AÑADIR PRODUCTOS

    def add_product_to_cart(self, product_id):
        button = self.page.locator(
            f'[data-test="add-to-cart-{product_id}"]'
        )
        button.click()

    def add_backpack_to_cart(self):
        self.add_product_to_cart("sauce-labs-backpack")

    def add_bike_light_to_cart(self):
        self.add_product_to_cart("sauce-labs-bike-light")

    def add_bolt_t_shirt_to_cart(self):
        self.add_product_to_cart("sauce-labs-bolt-t-shirt")

    def add_fleece_jacket_to_cart(self):
        self.add_product_to_cart("sauce-labs-fleece-jacket")

    def add_onesie_to_cart(self):
        self.add_product_to_cart("sauce-labs-onesie")

    def add_red_t_shirt_to_cart(self):
        self.add_product_to_cart(
            "test.allthethings()-t-shirt-(red)"
        )

    # CONSULTAS

    def get_page_title(self):
        return self.page_title.inner_text()

    def get_product_count(self):
        return self.product_items.count()

    def get_product_names(self):
        return self.product_names.all_inner_texts()

    def get_cart_count(self):
        if self.shopping_cart_badge.count() == 0:
            return 0

        return int(self.shopping_cart_badge.inner_text())

    # VERIFICACIONES

    def verify_products_page_is_visible(self):
        expect(self.product_list).to_be_visible()

    def verify_products_count(self, expected_count):
        expect(self.product_items).to_have_count(expected_count)

    def verify_page_title(self):
        expect(self.page_title).to_have_text("Products")

    def verify_cart_count(self, expected_count):
        if expected_count == 0:
            expect(self.shopping_cart_badge).to_have_count(0)
        else:
            expect(self.shopping_cart_badge).to_have_text(
                str(expected_count)
            )
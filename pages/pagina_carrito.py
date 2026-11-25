
from common.helpers import pausa


class PaginaCarrito:

    def __init__(self, page):
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
        self.product_quantities = page.locator(
            ".cart_quantity"
        )

        # BOTONES
        self.continue_shopping_button = page.locator(
            '[data-test="continue-shopping"]'
        )
        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )

        # BOTONES PARA ELIMINAR PRODUCTOS
        self.remove_backpack = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        )
        self.remove_bike_light = page.locator(
            '[data-test="remove-sauce-labs-bike-light"]'
        )
        self.remove_bolt_t_shirt = page.locator(
            '[data-test="remove-sauce-labs-bolt-t-shirt"]'
        )
        self.remove_fleece_jacket = page.locator(
            '[data-test="remove-sauce-labs-fleece-jacket"]'
        )
        self.remove_onesie = page.locator(
            '[data-test="remove-sauce-labs-onesie"]'
        )
        self.remove_red_t_shirt = page.locator(
            '[data-test="remove-test.allthethings()-t-shirt-(red)"]'
        )

    # ACCIONES

    def continue_shopping(self):
        self.continue_shopping_button.click()
        pausa(self.page, "Volvemos a todos los productos")

    def checkout(self):
        self.checkout_button.click()
        pausa(self.page, "Entramos en Checkout")

    def remove_backpack_from_cart(self):
        self.remove_backpack.click()
        pausa(self.page, "Mochila eliminada del carrito")

    def remove_bike_light_from_cart(self):
        self.remove_bike_light.click()
        pausa(self.page, "Luz de bicicleta eliminada")

    def remove_bolt_t_shirt_from_cart(self):
        self.remove_bolt_t_shirt.click()
        pausa(self.page, "Camiseta eliminada del carrito")

    def remove_fleece_jacket_from_cart(self):
        self.remove_fleece_jacket.click()
        pausa(self.page, "Chaqueta eliminada del carrito")

    def remove_onesie_from_cart(self):
        self.remove_onesie.click()
        pausa(self.page, "Mono eliminado del carrito")

    def remove_red_t_shirt_from_cart(self):
        self.remove_red_t_shirt.click()
        pausa(self.page, "Camiseta roja eliminada")

    def open_backpack_details(self):
        self.page.locator(
        '[data-test="item-4-title-link"]'
        ).click()

        pausa(self.page, "Volvemos al producto Sauce Labs Backpack")

    # COMPROBACIONES

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

    def is_backpack_visible(self):
        return self.page.locator(
        '[data-test="item-4-title-link"]'
        ).is_visible()

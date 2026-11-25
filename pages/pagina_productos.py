from common.helpers import pausa


class PaginaProductos:

    def __init__(self, page):
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
        self.shopping_cart_badge = page.locator(
            ".shopping_cart_badge"
        )

        # SELECTORES DE LOS SEIS PRODUCTOS
        self.backpack = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.bike_light = page.locator(
            '[data-test="add-to-cart-sauce-labs-bike-light"]'
        )
        self.bolt_t_shirt = page.locator(
            '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
        )
        self.fleece_jacket = page.locator(
            '[data-test="add-to-cart-sauce-labs-fleece-jacket"]'
        )
        self.onesie = page.locator(
            '[data-test="add-to-cart-sauce-labs-onesie"]'
        )
        self.red_t_shirt = page.locator(
            '[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]'
        )

    # ACCIONES GENERALES

    def wait_for_products(self):
        self.product_list.wait_for(state="visible")
        pausa(self.page, "Listado de productos visible")

    def open_cart(self):
        self.shopping_cart.click()
        pausa(self.page, "Carrito abierto")

    def select_sort_option(self, option):
        self.sort_dropdown.select_option(option)
        pausa(self.page, "Productos ordenados")

    # AÑADIR PRODUCTOS

    def add_backpack_to_cart(self):
        self.backpack.click()
        pausa(self.page, "Mochila añadida al carrito")

    def add_bike_light_to_cart(self):
        self.bike_light.click()
        pausa(self.page, "Luz de bicicleta añadida al carrito")

    def add_bolt_t_shirt_to_cart(self):
        self.bolt_t_shirt.click()
        pausa(self.page, "Camiseta añadida al carrito")

    def add_fleece_jacket_to_cart(self):
        self.fleece_jacket.click()
        pausa(self.page, "Chaqueta añadida al carrito")

    def add_onesie_to_cart(self):
        self.onesie.click()
        pausa(self.page, "Mono añadido al carrito")

    def add_red_t_shirt_to_cart(self):
        self.red_t_shirt.click()
        pausa(self.page, "Camiseta roja añadida al carrito")

    # COMPROBACIONES

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


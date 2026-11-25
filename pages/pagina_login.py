from common.helpers import pausa


class PaginaLogin:

    def __init__(self, page):
        self.page = page

        # SELECTORES
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

        # ACCIONES

    def open(self):
        self.page.goto("https://www.saucedemo.com/")
        pausa(self.page, "Página de login abierta")

    def enter_username(self, username):
        self.username.wait_for(state="visible")
        self.username.fill(username)
        pausa(self.page, "Usuario introducido")

    def enter_password(self, password):
        self.password.fill(password)
        pausa(self.page, "Contraseña introducida")

    def click_login(self):
        self.login_button.click()
        pausa(self.page, "Botón Login pulsado")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        # Esperar a que cargue el catálogo
        self.page.locator(".inventory_list").wait_for(
            state="visible"
        )

        pausa(self.page, "Login realizado correctamente")

    # COMPROBACIONES

    def get_error_message(self):
        return self.error_message.inner_text()

    def is_login_button_visible(self):
        return self.login_button.is_visible()

    def is_username_visible(self):
        return self.username.is_visible()

    def is_login_form_visible(self):
        return (
        self.username.is_visible()
        and self.password.is_visible()
        and self.login_button.is_visible()
        )

    def is_products_page_visible(self):
        return self.page.locator(".inventory_list").is_visible()

    def get_url(self):
        return self.page.url

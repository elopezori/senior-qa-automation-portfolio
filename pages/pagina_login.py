
from playwright.sync_api import Page, expect


class PaginaLogin:

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page

        # SELECTORES
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')
        self.products_list = page.locator(".inventory_list")

    # NAVEGACIÓN

    def open(self):
        self.page.goto(self.URL)

    # ACCIONES

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # COMPROBACIONES

    def get_error_message(self):
        return self.error_message.inner_text()

    def is_login_form_visible(self):
        return (
            self.username.is_visible()
            and self.password.is_visible()
            and self.login_button.is_visible()
        )

    def is_products_page_visible(self):
        return self.products_list.is_visible()

    def get_url(self):
        return self.page.url

    def verify_products_page(self):
        expect(self.products_list).to_be_visible()

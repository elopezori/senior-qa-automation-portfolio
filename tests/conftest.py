
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    try:
        page = context.new_page()
        yield page
    finally:
        context.close()
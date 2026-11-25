# 03. PLAYWRIGHT

## ¿Qué es Playwright?

Playwright es una herramienta de automatización que permite controlar navegadores y realizar pruebas de aplicaciones web.

En nuestro proyecto utilizamos Python y Chromium.

## Instalar Playwright

```powershell
python -m pip install playwright
```

## Instalar los navegadores

```powershell
python -m playwright install
```

## Instalar solamente Chromium

```powershell
python -m playwright install chromium
```

## Comprobar la instalación

```powershell
python -m playwright --version
```

## Importar Playwright en Python

```python
from playwright.sync_api import sync_playwright
```

## Ejemplo básico de automatización

```python
from playwright.sync_api import sync_playwright

def test_pagina():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://example.com")

        assert page.title() == "Example Domain"

        browser.close()
```

## Ejecutar en modo visual

```python
browser = p.chromium.launch(headless=False)
```

## Ejecutar en segundo plano

```python
browser = p.chromium.launch(headless=True)
```

## Captura de pantalla

```python
page.screenshot(path="captura.png")
```

## Buenas prácticas

- Utilizar localizadores fiables.
- Evitar esperas fijas innecesarias.
- Comprobar resultados mediante assertions.
- Cerrar correctamente el navegador.
- Mantener los tests independientes.

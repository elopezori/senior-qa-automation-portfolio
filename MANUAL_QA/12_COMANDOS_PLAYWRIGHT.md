# 12. COMANDOS PLAYWRIGHT

## ¿Qué es Playwright?

Playwright permite automatizar navegadores para comprobar el funcionamiento de aplicaciones web.

En nuestro proyecto utilizamos Python y Chromium.

## Instalar Playwright

```powershell
python -m pip install playwright
```

## Instalar navegadores

```powershell
python -m playwright install
```

## Instalar Chromium

```powershell
python -m playwright install chromium
```

## Instalar dependencias del navegador

```powershell
python -m playwright install-deps chromium
```

Este último comando está orientado principalmente a sistemas Linux.

## Consultar versión

```powershell
python -m playwright --version
```

## Ejecutar Chromium desde Python

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://example.com")

    print(page.title())

    browser.close()
```

## Modo headless

```python
browser = p.chromium.launch(headless=True)
```

## Modo visual

```python
browser = p.chromium.launch(headless=False)
```

## Capturar pantalla

```python
page.screenshot(path="captura.png")
```

## Capturar página completa

```python
page.screenshot(path="captura_completa.png", full_page=True)
```

## Navegar a una página

```python
page.goto("https://example.com")
```

## Obtener el título

```python
print(page.title())
```

## Localizar elementos

```python
page.get_by_role("button", name="Enviar")
page.get_by_label("Correo electrónico")
page.get_by_text("Bienvenido")
```

## Hacer clic

```python
page.get_by_role("button", name="Enviar").click()
```

## Introducir texto

```python
page.get_by_label("Correo electrónico").fill("test@example.com")
```

## Cerrar navegador

```python
browser.close()
```

## Recomendación

Utilizar localizadores estables y las esperas automáticas de Playwright.

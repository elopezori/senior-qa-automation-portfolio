# QA Automation Framework

Proyecto personal de QA Automation desarrollado con **Python, Playwright y Pytest**.

El objetivo es practicar y aplicar conceptos de automatización de pruebas web mediante una arquitectura organizada con Page Object Model (POM), ejecución de pruebas y generación de informes dinámicos basados en resultados reales.

## Tecnologías utilizadas

- Python
- Playwright
- Pytest
- pytest-json-report
- HTML y CSS
- PowerShell
- Git

## Funcionalidades

- Automatización de pruebas web con Playwright.
- Organización del código mediante Page Object Model (POM).
- Pruebas de navegación, búsqueda, inicio de sesión y carrito de compra.
- Ejecución de pruebas mediante Pytest.
- Generación de resultados estructurados en formato JSON.
- Generación de un dashboard HTML a partir de los resultados reales.
- Cálculo de estadísticas de ejecución.
- Script PowerShell para automatizar la ejecución y generación de informes.
- Documentación de procedimientos y comandos QA.

## Estructura del proyecto

```text
playwright_learning/
│
├── common/
│   ├── __init__.py
│   └── helpers.py
│
├── MANUAL_QA/
│   ├── 00_INDICE.md
│   ├── 01_ENTORNO_VIRTUAL.md
│   ├── ...
│   └── 15_CHECKLIST_QA.md
│
├── pages/
│   ├── __init__.py
│   ├── detalle_producto.py
│   ├── google_page.py
│   ├── pagina_login.py
│   ├── pagina_productos.py
│   ├── pagina_carrito.py
│   └── pagina_checkout.py
│
├── reporting/
│   ├── __init__.py
│   └── generate_report.py
│
├── tests/
│   ├── conftest.py
│   ├── test_01_open_page.py
│   ├── test_02_google_search.py
│   ├── test_03_login.py
│   ├── test_04_add_to_cart.py
│   └── test_05_manual_testing.py
│
├── requirements.txt
├── run_tests.ps1
├── README.md
└── .gitignore
```

## Requisitos previos

- Python instalado.
- Git instalado.
- PowerShell.
- Visual Studio Code (recomendado).

## Instalación

Clonar el repositorio:

```powershell
git clone URL_DEL_REPOSITORIO
cd playwright_learning
```

Crear el entorno virtual:

```powershell
python -m venv venv
```

Activar el entorno virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

Instalar Chromium para Playwright:

```powershell
python -m playwright install chromium
```

## Ejecución de las pruebas

Para ejecutar todos los tests y generar automáticamente los informes:

```powershell
.\run_tests.ps1
```

El script realiza las siguientes operaciones:

1. Ejecuta las pruebas con Pytest.
2. Genera el archivo JSON con los resultados.
3. Ejecuta el generador del dashboard.
4. Abre automáticamente el informe HTML.

## Informes y dashboard

Los resultados se generan en la carpeta `reports/`:

- `results.json`: resultados estructurados generados por Pytest.
- `report.html`: dashboard HTML generado a partir de los resultados reales.

El dashboard calcula estadísticas como el total de pruebas, pruebas superadas, fallidas, omitidas y duración.

La carpeta `reports/` está excluida de Git porque contiene resultados generados durante la ejecución.

## Ejecución manual

Ejecutar los tests:

```powershell
python -m pytest .\tests -v -s
```

Generar el informe JSON:

```powershell
python -m pytest .\tests -v -s --json-report --json-report-file=reports/results.json
```

Generar el dashboard:

```powershell
python .\reporting\generate_report.py
```

Abrir el dashboard:

```powershell
Start-Process .\reports\report.html
```

## Documentación

El proyecto incluye un manual con procedimientos, comandos y explicaciones sobre:

- Entorno virtual y Python.
- Playwright y Pytest.
- Ejecución de pruebas.
- Informes y dashboard QA.
- PowerShell y Git.
- Buenas prácticas y solución de errores.

Consulta el [índice del manual QA](MANUAL_QA/00_INDICE.md).

## Estado del proyecto

Proyecto personal de aprendizaje y práctica de QA Automation.

La suite actual contiene cinco pruebas de ejemplo. Una de ellas corresponde a un flujo de interacción manual, por lo que su resultado no debe interpretarse como una validación completamente automatizada.

## Autoría

Proyecto personal desarrollado como parte de mi aprendizaje en QA Automation.

# QA Automation Framework

Framework de automatización de pruebas web desarrollado con **Python, Playwright y Pytest**, siguiendo buenas prácticas de diseño, organización y mantenibilidad del código.

Este proyecto forma parte de mi portfolio de QA Automation y demuestra la implementación de una solución de automatización desde su estructura inicial hasta la ejecución de pruebas y generación de informes.

El objetivo es construir una arquitectura escalable, reutilizable y fácil de mantener, aplicando conceptos utilizados en proyectos reales de QA Automation.

## Tecnologías y herramientas

- **Python** – Lenguaje de programación.
- **Playwright** – Automatización de navegadores.
- **Pytest** – Framework de ejecución y gestión de pruebas.
- **Page Object Model (POM)** – Patrón de diseño para separar páginas y lógica de pruebas.
- **Pytest JSON Report** – Generación de resultados estructurados.
- **HTML5 y CSS3** – Construcción del dashboard de resultados.
- **PowerShell** – Automatización del proceso de ejecución.
- **Git** – Control de versiones.

## Arquitectura del proyecto

El proyecto está organizado por responsabilidades para facilitar la reutilización del código y el mantenimiento de la suite.

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

## Diseño y organización

### Page Object Model (POM)

La interacción con las páginas web está encapsulada en clases independientes.

Cada Page Object contiene:

- Localizadores de los elementos de la interfaz.
- Métodos para realizar acciones.
- Métodos de consulta.
- Verificaciones de estado de la página.

Esto permite mantener los tests separados de los detalles de implementación de la interfaz.

### Gestión del navegador y fixtures

La configuración de Pytest se centraliza en `tests/conftest.py`.

Se utilizan fixtures para:

- Inicializar Playwright.
- Gestionar el ciclo de vida del navegador.
- Crear contextos y páginas independientes para cada test.
- Garantizar la liberación de recursos mediante `try/finally`.

### Separación de responsabilidades

El proyecto diferencia las siguientes capas:

- `pages/`: interacción con las páginas web.
- `tests/`: escenarios y validaciones automatizadas.
- `common/`: utilidades compartidas.
- `reporting/`: procesamiento de resultados y generación del dashboard.
- `MANUAL_QA/`: documentación técnica y procedimientos QA.

## Funcionalidades implementadas

- Automatización de navegación web.
- Interacción con formularios.
- Validación de elementos de interfaz.
- Automatización del inicio de sesión.
- Gestión del carrito de compra.
- Verificación de productos añadidos y eliminados.
- Uso de aserciones de Playwright.
- Gestión de esperas automáticas.
- Registro de información mediante logging.
- Ejecución de pruebas mediante Pytest.
- Generación de informes JSON.
- Generación dinámica de un dashboard HTML.
- Cálculo de estadísticas de ejecución.
- Automatización del flujo completo mediante PowerShell.

## Requisitos previos

- Python 3.10 o superior.
- Git.
- PowerShell.
- Visual Studio Code (recomendado).

## Instalación y configuración

### 1. Clonar el repositorio

```powershell
git clone https://github.com/elopezori/senior-qa-automation-portfolio.git
```

Acceder a la carpeta del proyecto:

```powershell
cd senior-qa-automation-portfolio/playwright_learning
```

### 2. Crear el entorno virtual

```powershell
python -m venv venv
```

### 3. Activar el entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Instalar dependencias

```powershell
python -m pip install -r requirements.txt
```

### 5. Instalar Chromium para Playwright

```powershell
python -m playwright install chromium
```

## Ejecución de las pruebas

Para ejecutar la suite completa:

```powershell
.\run_tests.ps1
```

El script automatiza el siguiente proceso:

1. Comprueba la disponibilidad de Python y Pytest.
2. Prepara la carpeta de informes.
3. Ejecuta los tests mediante Pytest.
4. Genera el informe de resultados en JSON.
5. Ejecuta el generador del dashboard HTML.
6. Abre automáticamente el informe generado.
7. Devuelve el código de salida correspondiente al resultado de la ejecución.

## Informes de ejecución

Los informes se generan automáticamente en la carpeta `reports/`.

| Archivo | Descripción |
|---|---|
| `results.json` | Resultados estructurados de Pytest. |
| `report.html` | Dashboard visual generado a partir de los resultados. |

El dashboard presenta información como:

- Total de pruebas ejecutadas.
- Pruebas superadas.
- Pruebas fallidas.
- Pruebas omitidas.
- Porcentaje de éxito.
- Duración de la ejecución.
- Detalle de los resultados.

Los informes son artefactos generados durante la ejecución y no forman parte del código fuente versionado.

## Ejecución manual de Pytest

También es posible ejecutar los tests directamente:

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

Abrir el informe:

```powershell
Start-Process .\reports\report.html
```

## Estado actual del proyecto

**Última ejecución validada:**

| Métrica | Resultado |
|---|---:|
| Tests recopilados | 5 |
| Tests superados | 5 |
| Tests fallidos | 0 |
| Tests omitidos | 0 |
| Tiempo de ejecución | 8.93 segundos |

La suite incluye escenarios de navegación, transición entre sitios, autenticación y gestión del carrito.

El test `test_05_manual_testing.py` automatiza un flujo de preparación y deja disponible la opción de pausar el navegador para realizar exploración manual.

Estos resultados corresponden a una ejecución local y no representan todavía una integración continua (CI/CD).

## Documentación QA

El proyecto incluye un manual técnico en `MANUAL_QA/` con documentación sobre:

- Configuración del entorno.
- Python y entornos virtuales.
- Playwright y Pytest.
- Arquitectura y ejecución de pruebas.
- Generación de informes.
- PowerShell y Git.
- Buenas prácticas de QA.
- Resolución de problemas.

Consulta el [índice del manual QA](MANUAL_QA/00_INDICE.md).

## Objetivo profesional

Este proyecto tiene como objetivo demostrar conocimientos prácticos de automatización de pruebas, diseño de frameworks, organización de código, validación de aplicaciones web y generación de informes.

La prioridad es desarrollar una solución mantenible y ampliable, aplicando criterios de calidad y buenas prácticas de ingeniería de pruebas.

## Autoría

Proyecto personal desarrollado como parte de mi portfolio de QA Automation.
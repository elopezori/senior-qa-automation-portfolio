# 06. ARCHIVOS Y CARPETAS

## Objetivo

Conocer la estructura del proyecto y la función de cada archivo.

## Estructura de referencia

```text
playwright_learning/
│
├── venv/
│
├── tests/
│   ├── test_login.py
│   └── test_home.py
│
├── reports/
│   └── report.json
│
├── MANUAL_QA/
│   ├── 00_INDICE.md
│   ├── 01_ENTORNO_VIRTUAL.md
│   ├── 02_PYTHON_Y_PIP.md
│   ├── 03_PLAYWRIGHT.md
│   ├── 04_EJECUCION_TESTS.md
│   ├── 05_INFORMES_RESULTADOS.md
│   ├── 06_ARCHIVOS_Y_CARPETAS.md
│   ├── 07_VISUAL_STUDIO_CODE.md
│   ├── 08_BUENAS_PRACTICAS.md
│   └── 09_DASHBOARD_QA.md
│
├── requirements.txt
├── pytest.ini
├── conftest.py
└── README.md
```

Esta estructura es orientativa y debe adaptarse a los archivos reales del proyecto.

## Crear carpetas

```powershell
New-Item -ItemType Directory -Path ".\tests" -Force
New-Item -ItemType Directory -Path ".\reports" -Force
New-Item -ItemType Directory -Path ".\pages" -Force
New-Item -ItemType Directory -Path ".\utils" -Force
```

## Mostrar estructura de carpetas

```powershell
tree /F
```

## Listar archivos

```powershell
Get-ChildItem
```

## Buscar archivos Python

```powershell
Get-ChildItem -Recurse -Filter "*.py"
```

## Buscar archivos JSON

```powershell
Get-ChildItem -Recurse -Filter "*.json"
```

## Crear un archivo Python

```powershell
New-Item -ItemType File -Path ".\tests\test_example.py" -Force
```

## Crear archivo requirements

```powershell
New-Item -ItemType File -Path ".\requirements.txt" -Force
```

## Recomendación

Separar tests, informes, documentación y utilidades para mantener un proyecto ordenado.

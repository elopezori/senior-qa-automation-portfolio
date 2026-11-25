# 09. DASHBOARD QA

## ¿Qué es el Dashboard QA?

Es una interfaz visual que permite consultar los resultados de las pruebas automatizadas.

Su objetivo es facilitar el seguimiento del estado de las ejecuciones y mostrar información relevante de forma clara.

## Tecnologías utilizadas

- Python: procesamiento de los resultados.
- Pytest: ejecución de las pruebas automatizadas.
- pytest-json-report: generación de resultados en formato JSON.
- HTML: estructura del informe visual.
- CSS: diseño y presentación del dashboard.
- JavaScript: funcionalidades visuales incluidas en el informe.

## Funcionamiento en este proyecto

El dashboard se genera automáticamente a partir de los resultados reales de Pytest.

El proceso es el siguiente:

1. Ejecutar los tests con Pytest.
2. Generar el archivo JSON con los resultados.
3. Procesar el JSON mediante el generador de informes.
4. Calcular las estadísticas de ejecución.
5. Generar el dashboard HTML.
6. Abrir el informe en el navegador.

## Archivos utilizados

```text
playwright_learning/
│
├── reporting/
│   ├── __init__.py
│   └── generate_report.py
│
├── reports/
│   ├── results.json
│   └── report.html
│
└── run_tests.ps1
```

La carpeta `reports` se genera durante la ejecución y está excluida del repositorio mediante `.gitignore`.

## Generar el JSON de resultados

```powershell
New-Item -ItemType Directory -Path ".\reports" -Force

python -m pytest .\tests -v -s --json-report --json-report-file=reports/results.json
```

## Generar el dashboard

```powershell
python .\reporting\generate_report.py
```

## Abrir el dashboard

```powershell
Start-Process .\reports\report.html
```

## Ejecutar todo el proceso automáticamente

El proyecto dispone de un script que ejecuta las pruebas, genera el JSON, crea el dashboard y abre el informe:

```powershell
.\run_tests.ps1
```

## Indicadores principales

El dashboard procesa los resultados reales y muestra indicadores como:

- Total de tests ejecutados.
- Tests superados.
- Tests fallidos.
- Tests omitidos.
- Porcentaje de éxito.
- Duración de las pruebas.

## Información de los tests

El informe también permite consultar el detalle de las pruebas y sus resultados.

Los datos proceden del informe JSON generado por Pytest, no de valores introducidos manualmente.

## Importante sobre los informes

- `results.json`: contiene los resultados de la ejecución.
- `report.html`: contiene el dashboard visual generado a partir del JSON.

Cada nueva ejecución mediante `run_tests.ps1` actualiza los informes con los resultados de esa ejecución.

## Objetivo

Disponer de un panel visual basado en datos reales que permita analizar rápidamente la calidad y el estado de las pruebas automatizadas.

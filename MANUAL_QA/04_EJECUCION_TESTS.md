# 04. EJECUCIÓN DE TESTS

## ¿Qué es Pytest?

Pytest es un framework de Python que permite ejecutar pruebas automatizadas y comprobar sus resultados.

## Ejecutar todos los tests

```powershell
python -m pytest .\tests
```

## Ejecutar mostrando los nombres de los tests

```powershell
python -m pytest .\tests -v
```

## Ejecutar mostrando información adicional

```powershell
python -m pytest .\tests -vv
```

## Ejecutar un archivo específico

```powershell
python -m pytest .\tests\test_03_login.py -v
```

## Ejecutar tests por nombre

```powershell
python -m pytest .\tests -k "login"
```

## Mostrar los prints durante la ejecución

```powershell
python -m pytest .\tests -v -s
```

## Ejecutar toda la batería con detalle

```powershell
python -m pytest .\tests -v -s
```

## Resultado esperado

Pytest muestra un resumen con:

- PASSED: pruebas superadas.
- FAILED: pruebas fallidas.
- ERROR: errores durante la preparación o ejecución.
- SKIPPED: pruebas omitidas.

## Ejecutar todos los tests y generar el dashboard

El proyecto incluye un script de PowerShell que automatiza el proceso completo:

```powershell
.\run_tests.ps1
```

Este script:

1. Ejecuta los tests con Pytest.
2. Genera el archivo JSON con los resultados.
3. Ejecuta el generador del dashboard.
4. Abre automáticamente el informe HTML.

## Generar el JSON de resultados manualmente

```powershell
python -m pytest .\tests -v -s --json-report --json-report-file=reports/results.json
```

## Generar el dashboard manualmente

```powershell
python .\reporting\generate_report.py
```

## Abrir el dashboard

```powershell
Start-Process .\reports\report.html
```

## Ubicación de los informes

Los informes se guardan en la carpeta `reports`:

- `results.json`: resultados generados por Pytest.
- `report.html`: dashboard HTML generado a partir de los resultados reales.

Esta carpeta está excluida del repositorio mediante `.gitignore`.

## Recomendación

Antes de publicar cambios en el proyecto, ejecutar la batería completa y comprobar que los resultados del dashboard coinciden con los resultados de Pytest.

# 05. INFORMES Y RESULTADOS

## Objetivo

Registrar los resultados de las pruebas automatizadas para facilitar su análisis y seguimiento.

## Generar informe JSON

Primero instalar el plugin:

```powershell
python -m pip install pytest-json-report
```

Ejecutar:

```powershell
python -m pytest --json-report --json-report-file=reports/report.json
```

## Crear carpeta de informes

```powershell
New-Item -ItemType Directory -Path ".\reports" -Force
```

## Generar informe con información detallada

```powershell
python -m pytest -v --json-report --json-report-file=reports/report.json
```

## Consultar el informe

```powershell
Get-Content .\reports\report.json
```

## Abrir el informe con Visual Studio Code

```powershell
code .\reports\report.json
```

## Información que puede contener el JSON

- Número total de pruebas.
- Pruebas superadas.
- Pruebas fallidas.
- Pruebas omitidas.
- Duración de ejecución.
- Información de errores.
- Resultados individuales.

## Crear un nuevo informe

La ejecución puede sobrescribir el informe anterior. Si queremos conservar históricos, debemos generar nombres diferentes para cada ejecución.

## Importante

El informe JSON es el archivo de datos que posteriormente puede utilizar el Dashboard QA.

El dashboard deberá estar preparado para interpretar la estructura real del JSON generado por Pytest.

## Para ver el html de 

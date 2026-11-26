# 14. SOLUCIÓN DE ERRORES

## Objetivo

Recopilar los errores más habituales del proyecto QA Automation y sus posibles soluciones.

## Error: Python no reconocido

Mensaje habitual:

```text
python is not recognized
```

Solución:

1. Comprobar que Python está instalado.
2. Comprobar la variable PATH.
3. Reiniciar PowerShell.
4. Probar:

```powershell
py --version
```

## Error: No se puede activar el entorno virtual

Mensaje habitual:

```text
running scripts is disabled on this system
```

Solución temporal para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Después:

```powershell
.\venv\Scripts\Activate.ps1
```

## Error: No module named pytest

Solución:

```powershell
python -m pip install pytest
```

## Error: No module named playwright

Solución:

```powershell
python -m pip install playwright
```

## Error: Ejecutable de Chromium no encontrado

Solución:

```powershell
python -m playwright install chromium
```

## Error: pytest no encuentra los tests

Comprobar:

- Que los archivos comienzan por test_.
- Que las funciones comienzan por test_.
- Que estamos en la carpeta raíz.
- Que Pytest está instalado.

Ejecutar:

```powershell
python -m pytest --collect-only -v
```

## Error: No existe la carpeta reports

Solución:

```powershell
New-Item -ItemType Directory -Path ".\reports" -Force
```

## Error: No se encuentra pytest-json-report

Solución:

```powershell
python -m pip install pytest-json-report
```

## Error: No se encuentra el archivo report.json

Comprobar que se ha ejecutado:

```powershell
python -m pytest --json-report --json-report-file=reports/report.json
```

## Error: Dashboard sin datos

Comprobar:

1. Que existe report.json.
2. Que el JSON contiene resultados.
3. Que la ruta utilizada por JavaScript es correcta.
4. Que se ha iniciado un servidor HTTP local.
5. Que el dashboard interpreta la estructura real del informe.

## Error: Puerto ocupado

Iniciar el servidor en otro puerto:

```powershell
python -m http.server 8001 --directory dashboard
```

## Error: Test fallido

Ejecutar individualmente:

```powershell
python -m pytest tests/test_login.py -v -s
```

Revisar el mensaje de error, los localizadores y el estado de la aplicación.

## Recomendación

Registrar cada nuevo error y su solución para ampliar este documento con la experiencia del proyecto.

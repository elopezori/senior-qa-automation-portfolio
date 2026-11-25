# 11. COMANDOS PYTEST

## ¿Qué es Pytest?

Pytest es el framework utilizado para ejecutar y validar las pruebas automatizadas de nuestro proyecto.

## Ejecutar todos los tests

```powershell
python -m pytest
```

## Ejecución detallada

```powershell
python -m pytest -v
```

## Máximo detalle

```powershell
python -m pytest -vv
```

## Ejecutar un archivo

```powershell
python -m pytest tests/test_login.py
```

## Ejecutar una función concreta

```powershell
python -m pytest tests/test_login.py::test_login_correcto
```

## Buscar tests por nombre

```powershell
python -m pytest -k "login"
```

## Ejecutar tests por marcador

```powershell
python -m pytest -m smoke
```

## Ejecutar varios marcadores

```powershell
python -m pytest -m "smoke or regression"
```

## Mostrar los prints

```powershell
python -m pytest -s
```

## Detener al primer fallo

```powershell
python -m pytest -x
```

## Repetir pruebas fallidas

Requiere instalar pytest-rerunfailures:

```powershell
python -m pip install pytest-rerunfailures
```

Ejecutar:

```powershell
python -m pytest --reruns 2
```

## Ejecutar con informe JSON

```powershell
python -m pytest -v --json-report --json-report-file=reports/report.json
```

## Ejecutar con informe HTML

Requiere instalar pytest-html:

```powershell
python -m pip install pytest-html
```

Ejecutar:

```powershell
python -m pytest --html=reports/report.html --self-contained-html
```

## Consultar ayuda

```powershell
python -m pytest --help
```

## Consultar versión

```powershell
python -m pytest --version
```

## Recomendación

Ejecutar primero los tests de forma individual y después toda la batería completa.

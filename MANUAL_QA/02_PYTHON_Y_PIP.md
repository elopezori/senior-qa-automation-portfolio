# 02. PYTHON Y PIP

## ¿Qué es Python?

Python es el lenguaje utilizado para desarrollar nuestros scripts y pruebas automatizadas.

## ¿Qué es PIP?

PIP es el gestor de paquetes de Python. Permite instalar, actualizar y administrar librerías.

## Comprobar la versión de Python

```powershell
python --version
```

## Comprobar PIP

```powershell
python -m pip --version
```

## Actualizar PIP

```powershell
python -m pip install --upgrade pip
```

## Instalar Pytest

```powershell
python -m pip install pytest
```

## Instalar Playwright

```powershell
python -m pip install playwright
```

## Instalar el plugin para informes JSON

```powershell
python -m pip install pytest-json-report
```

## Consultar paquetes instalados

```powershell
python -m pip list
```

## Guardar dependencias

```powershell
python -m pip freeze > requirements.txt
```

## Instalar dependencias desde requirements.txt

```powershell
python -m pip install -r requirements.txt
```

## Desinstalar un paquete

```powershell
python -m pip uninstall nombre_paquete
```

## Recomendación

Trabajar siempre con el entorno virtual activado antes de instalar dependencias.

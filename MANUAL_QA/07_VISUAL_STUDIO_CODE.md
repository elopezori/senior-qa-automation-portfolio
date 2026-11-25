# 07. VISUAL STUDIO CODE

## ¿Qué es Visual Studio Code?

Es el editor de código utilizado para desarrollar y gestionar nuestro proyecto QA Automation.

## Abrir el proyecto

Desde PowerShell:

```powershell
code .
```

## Abrir una carpeta concreta

```powershell
code .\MANUAL_QA
```

## Abrir un archivo

```powershell
code .\MANUAL_QA\00_INDICE.md
```

## Extensiones recomendadas

- Python.
- Pylance.
- Python Debugger.
- Playwright Test for VSCode, si se trabaja también con proyectos JavaScript o TypeScript.

## Seleccionar intérprete Python

1. Abrir Visual Studio Code.
2. Pulsar Ctrl + Shift + P.
3. Buscar Python: Select Interpreter.
4. Seleccionar el intérprete de la carpeta venv.

## Abrir terminal integrado

Atajo:

```text
Ctrl + `
```

## Activar entorno virtual desde VS Code

```powershell
.\venv\Scripts\Activate.ps1
```

## Ejecutar tests desde terminal

```powershell
python -m pytest -v
```

## Abrir documentación Markdown

Seleccionar un archivo .md.

Para abrir la vista previa:

```text
Ctrl + Shift + V
```

## Recomendación

Utilizar la terminal integrada para ejecutar comandos y la vista previa Markdown para consultar el manual.

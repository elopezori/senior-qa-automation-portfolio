# 01. ENTORNO VIRTUAL

## ¿Qué es un entorno virtual?

Es un espacio independiente donde instalamos las librerías necesarias para nuestro proyecto Python.

Permite evitar conflictos entre versiones de paquetes de diferentes proyectos.

## Crear el entorno virtual

Desde la carpeta principal:

```powershell
python -m venv venv
```

## Activar el entorno virtual

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## Comprobar que está activado

El terminal debe mostrar:

```text
(venv) PS C:\Users\admin\playwright_learning>
```

También podemos comprobar Python:

```powershell
python --version
```

## Desactivar el entorno virtual

```powershell
deactivate
```

## Eliminar el entorno virtual

Primero desactivarlo y después:

```powershell
Remove-Item -Recurse -Force .\venv
```

## Crear un nuevo entorno virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

## Importante

La carpeta venv no debe subirse normalmente a Git.

Debe incluirse en el archivo .gitignore.

# 13. COMANDOS GIT

## ¿Qué es Git?

Git es un sistema de control de versiones que permite registrar cambios y mantener un historial del proyecto.

## Comprobar instalación

```powershell
git --version
```

## Inicializar repositorio

```powershell
git init
```

## Consultar estado

```powershell
git status
```

## Añadir todos los archivos

```powershell
git add .
```

## Añadir un archivo específico

```powershell
git add tests/test_login.py
```

## Guardar cambios

```powershell
git commit -m "Añadir pruebas automatizadas"
```

## Consultar historial

```powershell
git log
```

## Historial resumido

```powershell
git log --oneline
```

## Crear una rama

```powershell
git branch nueva-funcionalidad
```

## Cambiar de rama

```powershell
git switch nueva-funcionalidad
```

## Crear y cambiar de rama

```powershell
git switch -c nueva-funcionalidad
```

## Consultar ramas

```powershell
git branch
```

## Actualizar información del repositorio remoto

```powershell
git fetch
```

## Descargar cambios

```powershell
git pull
```

## Enviar cambios

```powershell
git push
```

## Consultar diferencias

```powershell
git diff
```

## Crear archivo .gitignore

```powershell
New-Item -ItemType File -Path ".gitignore" -Force
```

Contenido recomendado para .gitignore:

```text
venv/
__pycache__/
.pytest_cache/
*.pyc
.env
reports/
```

Si queremos conservar los informes JSON o los históricos en Git, no debemos ignorar reports/.

## Recomendación

Realizar commits pequeños, claros y descriptivos.

No subir contraseñas, tokens ni información sensible al repositorio.

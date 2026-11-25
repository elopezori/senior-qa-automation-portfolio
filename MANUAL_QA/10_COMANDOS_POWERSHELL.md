# 10. COMANDOS POWERSHELL

## ¿Qué es PowerShell?

PowerShell es la terminal que utilizamos en Windows para ejecutar comandos, administrar archivos y controlar nuestro proyecto.

## Navegación

Mostrar carpeta actual:

```powershell
Get-Location
```

Listar archivos:

```powershell
Get-ChildItem
```

Entrar en una carpeta:

```powershell
Set-Location .\tests
```

Volver a la carpeta anterior:

```powershell
Set-Location ..
```

Volver a la raíz del proyecto:

```powershell
Set-Location C:\Users\admin\playwright_learning
```

## Crear carpetas

```powershell
New-Item -ItemType Directory -Path ".\reports" -Force
```

## Crear archivos

```powershell
New-Item -ItemType File -Path ".\archivo.txt" -Force
```

## Eliminar archivos

```powershell
Remove-Item .\archivo.txt
```

## Eliminar carpetas

```powershell
Remove-Item .\carpeta -Recurse -Force
```

Cuidado: esta operación elimina el contenido de la carpeta.

## Copiar archivos

```powershell
Copy-Item .\archivo.txt .\reports\
```

## Mover archivos

```powershell
Move-Item .\archivo.txt .\reports\
```

## Renombrar archivos

```powershell
Rename-Item .\archivo.txt archivo_nuevo.txt
```

## Buscar archivos Python

```powershell
Get-ChildItem -Recurse -Filter "*.py"
```

## Buscar archivos JSON

```powershell
Get-ChildItem -Recurse -Filter "*.json"
```

## Mostrar estructura completa

```powershell
tree /F
```

## Limpiar terminal

```powershell
Clear-Host
```

## Abrir Visual Studio Code

```powershell
code .
```

## Abrir el explorador de Windows

```powershell
explorer .
```

## Recomendación

Comprobar siempre la carpeta actual antes de ejecutar comandos que eliminen o modifiquen archivos.

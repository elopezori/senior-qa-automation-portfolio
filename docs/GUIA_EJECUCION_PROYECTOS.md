
# Guía de ejecución de proyectos
## Senior QA Automation Portfolio

Este documento recoge los comandos necesarios para ejecutar todos los proyectos del portfolio o ejecutar cada uno de forma independiente.

**Directorio raíz:**
`C:\Users\admin\playwright_learning`

**Entorno Python:** `venv`

---

## 1. Preparación del entorno

Abrir PowerShell en la raíz del portfolio.

Activar el entorno virtual de Python:

```powershell
.\venv\Scripts\Activate.ps1
```

Comprobar Python:

```powershell
python --version
```

Comprobar Pytest:

```powershell
python -m pytest --version
```

---

## 2. Ejecutar todos los proyectos

Ejecuta el siguiente comando desde la raíz:

```powershell
.\run_all_tests.ps1
```

Este script ejecuta automáticamente:

1. Selenium WebDriver + C#
2. Playwright + Python
3. Playwright + .NET
4. API Automation + Python

Al finalizar muestra un resumen con los proyectos correctos y los que han fallado.

---

## 3. Ejecutar proyectos individualmente

### Proyecto 01 - Selenium WebDriver + C#

Tecnologías:
- C#
- .NET
- Selenium WebDriver
- NUnit

Compilar:

```powershell
dotnet build .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
```

Ejecutar pruebas:

```powershell
dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
```

---

### Proyecto 02 - Playwright + Python

Tecnologías:
- Python
- Playwright
- Pytest
- Page Object Model

Ejecutar todas las pruebas:

```powershell
python -m pytest .\02_Automatizacion_Web_Playwright_Python\tests -v
```

Ejecutar el script automatizado:

```powershell
.\02_Automatizacion_Web_Playwright_Python\run_tests.ps1
```

El script genera:
- results.json
- report.html

Ubicación de los informes:

`02_Automatizacion_Web_Playwright_Python/reports/`

---

### Proyecto 03 - Playwright + .NET

Tecnologías:
- C#
- .NET 10
- Playwright
- NUnit

Compilar:

```powershell
dotnet build .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx
```

Ejecutar pruebas:

```powershell
dotnet test .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx
```

---

### Proyecto 04 - API Automation + Python

Tecnologías:
- Python
- Requests
- Pytest
- JSON Schema
- Allure
- HTML Reporting

Ejecutar todas las pruebas:

```powershell
python -m pytest .\04_Automatizacion_API_Python_Requests_Pytest -v
```

Generar resultados Allure:

```powershell
allure serve .\04_Automatizacion_API_Python_Requests_Pytest\allure-results
```

El proyecto también genera un informe HTML.

Ubicación:

`04_Automatizacion_API_Python_Requests_Pytest/reports/`

---

## 4. Ejecutar pruebas específicas

### Ejecutar un único archivo de tests

Ejemplo:

```powershell
python -m pytest .\04_Automatizacion_API_Python_Requests_Pytest\tests\test_users.py -v
```

### Ejecutar un test concreto

```powershell
python -m pytest .\04_Automatizacion_API_Python_Requests_Pytest\tests\test_users.py -k "get_user" -v
```

### Mostrar información detallada

```powershell
python -m pytest RUTA_DEL_PROYECTO -v -s
```

---

## 5. Informes y resultados

| Proyecto | Informe |
|---|---|
| 01 Selenium | Resultados en consola |
| 02 Playwright Python | reports/report.html |
| 03 Playwright .NET | Resultados en consola |
| 04 API Python | reports/api_test_report.html |

Los resultados de Allure se almacenan en:

`04_Automatizacion_API_Python_Requests_Pytest/allure-results/`

Para visualizar Allure:

```powershell
allure serve .\04_Automatizacion_API_Python_Requests_Pytest\allure-results
```

---

## 6. Comandos útiles de mantenimiento

### Consultar versión de .NET

```powershell
dotnet --version
```

### Consultar paquetes Python

```powershell
python -m pip list
```

### Instalar dependencias del proyecto 02

```powershell
python -m pip install -r .\02_Automatizacion_Web_Playwright_Python\requirements.txt
```

### Instalar dependencias del proyecto 04

```powershell
python -m pip install -r .\04_Automatizacion_API_Python_Requests_Pytest\requirements.txt
```

### Comprobar proyectos .NET

```powershell
dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
dotnet test .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx
```

---

## 7. Tabla resumen de comandos principales

| Objetivo | Comando |
|---|---|
| Ejecutar todo | `.\run_all_tests.ps1` |
| Selenium C# | `dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx` |
| Playwright Python | `.\02_Automatizacion_Web_Playwright_Python\run_tests.ps1` |
| Playwright .NET | `dotnet test .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx` |
| API Python | `python -m pytest .\04_Automatizacion_API_Python_Requests_Pytest -v` |

---

## 8. Buenas prácticas

- Ejecutar los comandos desde la raíz del portfolio, salvo que se indique lo contrario.
- Mantener actualizado el entorno virtual.
- Instalar las dependencias de cada proyecto cuando sea necesario.
- Revisar los informes HTML después de cada ejecución.
- No publicar credenciales ni información confidencial.
- Mantener actualizada esta guía cuando se incorporen nuevos proyectos.

---

**Senior QA Automation Portfolio**

Documento de referencia para la ejecución y mantenimiento de los proyectos.
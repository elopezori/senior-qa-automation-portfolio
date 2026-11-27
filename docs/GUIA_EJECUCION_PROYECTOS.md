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

**Tecnologías:**
- C#
- .NET 10
- Selenium WebDriver
- NUnit
- Allure NUnit
- Page Object Model (POM)

#### Estructura del proyecto

```text
01_Automatizacion_Web_Selenium_CSharp/
│
├── SeleniumAutomation.slnx
│
├── SeleniumAutomation.Tests/
│   ├── Configuration/
│   │   ├── BaseTest.cs
│   │   ├── BrowserSettings.cs
│   │   └── DriverFactory.cs
│   │
│   ├── Pages/
│   │   └── HomePage.cs
│   │
│   ├── Tests/
│   │   ├── Home/
│   │   │   └── HomePageTests.cs
│   │   └── Settings/
│   │       └── TestSettings.cs
│   │
│   ├── allureConfig.json
│   └── SeleniumAutomation.Tests.csproj
│
└── reports/
    └── allure-report/
```

#### Componentes principales

- `DriverFactory.cs`: creación y configuración de Chrome, Edge y Firefox.
- `BrowserSettings.cs`: habilitación y deshabilitación de navegadores.
- `BaseTest.cs`: inicialización del navegador, esperas y cierre de sesión de prueba. También gestiona capturas de pantalla cuando una prueba falla.
- `HomePage.cs`: implementación del patrón Page Object Model para la página principal.
- `HomePageTests.cs`: pruebas automatizadas de la página principal.
- `TestSettings.cs`: configuración general mediante variables de entorno.

#### Compilar el proyecto

```powershell
dotnet build .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
```

#### Ejecutar todas las pruebas

```powershell
dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx --logger "console;verbosity=normal"
```

La ejecución contempla los navegadores habilitados en:

`01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.Tests/Configuration/BrowserSettings.cs`

Actualmente están habilitados:

- Chrome
- Edge
- Firefox

Para activar o desactivar navegadores, modificar los valores `true` o `false` de:

- `RunChrome`
- `RunEdge`
- `RunFirefox`

Cada navegador habilitado genera un caso de prueba independiente.

#### Configuración mediante variables de entorno

El proyecto permite configurar determinados parámetros:

| Variable | Descripción | Valor predeterminado |
|---|---|---|
| `SELENIUM_BROWSER` | Navegador predeterminado cuando no se proporciona uno al test | Chrome |
| `SELENIUM_HEADLESS` | Ejecución sin interfaz gráfica | false |
| `SELENIUM_TIMEOUT` | Tiempo máximo de espera en segundos | 10 |
| `SELENIUM_BASE_URL` | URL base de la aplicación | https://the-internet.herokuapp.com/ |

Ejemplo para ejecutar las pruebas en modo headless:

```powershell
$env:SELENIUM_HEADLESS = "true"

dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
```

La variable `SELENIUM_HEADLESS` afecta a los navegadores habilitados.

Para volver a la configuración predeterminada:

```powershell
Remove-Item Env:SELENIUM_BROWSER -ErrorAction SilentlyContinue
Remove-Item Env:SELENIUM_HEADLESS -ErrorAction SilentlyContinue
Remove-Item Env:SELENIUM_TIMEOUT -ErrorAction SilentlyContinue
Remove-Item Env:SELENIUM_BASE_URL -ErrorAction SilentlyContinue
```

#### Resultados Allure

Los resultados de las pruebas se generan en:

`01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.Tests/TestResults/AllureResults/`

Antes de generar un reporte nuevo, se pueden limpiar los resultados anteriores:

```powershell
$allurePath = ".\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.Tests\TestResults\AllureResults"

Remove-Item "$allurePath\*" -Recurse -Force
```

**Generar el reporte HTML de Allure:**

```powershell
allure generate .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.Tests\TestResults\AllureResults --clean -o .\01_Automatizacion_Web_Selenium_CSharp\reports\allure-report
```

**Abrir el reporte generado:**

```powershell
allure open .\01_Automatizacion_Web_Selenium_CSharp\reports\allure-report
```

El reporte permite consultar:

- Resultados de las pruebas.
- Estado de cada ejecución.
- Navegador utilizado (Chrome, Edge o Firefox).
- Etiquetas, funcionalidades e historias de los tests.
- Capturas de pantalla adjuntas cuando se produce un fallo.

#### Capturas de pantalla automáticas

Cuando una prueba falla, `BaseTest.cs` intenta:

1. Obtener una captura de pantalla del navegador.
2. Guardarla en disco.
3. Adjuntarla al resultado de NUnit.
4. Adjuntarla al informe de Allure.

La ubicación física de las capturas es:

`SeleniumAutomation.Tests/bin/Debug/net10.0/TestResults/Screenshots/`

Esta ubicación corresponde al directorio de trabajo utilizado actualmente por NUnit durante la ejecución.

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
| 01 Selenium | Allure HTML + resultados JSON + capturas de pantalla |
| 02 Playwright Python | reports/report.html |
| 03 Playwright .NET | Resultados en consola |
| 04 API Python | reports/api_test_report.html |

Los resultados de Allure del Proyecto 01 se almacenan en:

`01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.Tests/TestResults/AllureResults/`

El reporte HTML generado se almacena en:

`01_Automatizacion_Web_Selenium_CSharp/reports/allure-report/`

Los resultados de Allure del Proyecto 04 se almacenan en:

`04_Automatizacion_API_Python_Requests_Pytest/allure-results/`

Para visualizar Allure del Proyecto 04:

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
| Generar reporte Allure Selenium | `allure generate .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.Tests\TestResults\AllureResults --clean -o .\01_Automatizacion_Web_Selenium_CSharp\reports\allure-report` |
| Abrir reporte Allure Selenium | `allure open .\01_Automatizacion_Web_Selenium_CSharp\reports\allure-report` |
| Playwright Python | `.\02_Automatizacion_Web_Playwright_Python\run_tests.ps1` |
| Playwright .NET | `dotnet test .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx` |
| API Python | `python -m pytest .\04_Automatizacion_API_Python_Requests_Pytest -v` |

---

## 8. Buenas prácticas

- Ejecutar los comandos desde la raíz del portfolio, salvo que se indique lo contrario.
- Mantener actualizado el entorno virtual.
- Instalar las dependencias de cada proyecto cuando sea necesario.
- Revisar los informes HTML después de cada ejecución.
- Limpiar los resultados anteriores de Allure antes de generar un nuevo reporte independiente.
- No publicar credenciales ni información confidencial.
- Mantener actualizada esta guía cuando se incorporen nuevos proyectos.

---

**Senior QA Automation Portfolio**

Documento de referencia para la ejecución y mantenimiento de los proyectos.
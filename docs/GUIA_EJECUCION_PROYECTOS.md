# Guía de ejecución de proyectos
## Senior QA Automation Portfolio

Este documento recoge los comandos necesarios para preparar el entorno, ejecutar todos los proyectos del portfolio o ejecutar cada uno de forma independiente.

El portfolio es compatible con **Windows y macOS**, utilizando PowerShell y los entornos virtuales propios de cada proyecto.

**Directorio raíz del repositorio:**

```text
senior-qa-automation-portfolio/
```

**Herramientas principales:**
- PowerShell 7
- .NET SDK 10
- Python 3
- Pytest
- Allure Commandline

---

## 1. Preparación del entorno

Abrir una terminal PowerShell situada en el directorio raíz del portfolio.

### Comprobar las herramientas

Ejecutar los siguientes comandos:

```powershell
dotnet --version
python --version
pwsh --version
allure --version
```

En macOS, si el comando `python` no está disponible, utilizar:

```bash
python3 --version
```

### Entornos virtuales de Python

Cada proyecto Python dispone de su propio entorno virtual `.venv`.

No es necesario activar manualmente los entornos para ejecutar el script central, ya que este utiliza directamente el Python de cada proyecto.

Si se desea ejecutar un proyecto Python manualmente, se puede activar su entorno correspondiente.

**Windows:**

```powershell
.\02_Automatizacion_Web_Playwright_Python\.venv\Scripts\Activate.ps1
```

**macOS:**

```bash
source ./02_Automatizacion_Web_Playwright_Python/.venv/bin/activate
```

Para el proyecto de API, sustituir la ruta por:

```text
04_Automatizacion_API_Python_Requests_Pytest/.venv/
```

Comprobar Python y Pytest:

```powershell
python --version
python -m pytest --version
```

---

## 2. Ejecutar todos los proyectos

El repositorio dispone de un ejecutor central que permite lanzar los cuatro proyectos consecutivamente y obtener un resumen general.

Ejecutar siempre desde la raíz del repositorio.

### Windows

```powershell
.\run_all_tests.ps1
```

### macOS

```bash
pwsh ./run_all_tests.ps1
```

El script ejecuta automáticamente:

1. Selenium WebDriver + C#
2. Playwright + Python
3. Playwright + .NET
4. API Automation + Python

Al finalizar muestra un resumen con el estado de cada proyecto:

- CORRECTO: todos los tests del proyecto han finalizado correctamente.
- ERROR: se ha producido algún error durante la ejecución.

También recopila los resultados de Allure y genera un informe conjunto.

### Informe Allure conjunto

El ejecutor central genera automáticamente el informe en:

```text
allure-report/
```

Los resultados recopilados se almacenan en:

```text
allure-results/
```

Actualmente, el informe conjunto incorpora los resultados de:

- Proyecto 01 - Selenium WebDriver + C#.
- Proyecto 04 - API Automation + Python.

Los proyectos 02 y 03 todavía no incorporan resultados al informe Allure conjunto.

El script intenta abrir automáticamente el informe al finalizar.

Para abrirlo manualmente:

```powershell
allure open allure-report
```

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
```

#### Componentes principales

- `DriverFactory.cs`: creación y configuración de Chrome, Edge y Firefox.
- `BrowserSettings.cs`: habilitación y deshabilitación de navegadores.
- `BaseTest.cs`: inicialización del navegador, esperas y cierre de sesión de prueba. También gestiona capturas de pantalla cuando una prueba falla.
- `HomePage.cs`: implementación del patrón Page Object Model para la página principal.
- `HomePageTests.cs`: pruebas automatizadas de la página principal.
- `TestSettings.cs`: configuración general mediante variables de entorno.

#### Compilar el proyecto

**Windows:**

```powershell
dotnet build .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
```

**macOS:**

```bash
dotnet build ./01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.slnx
```

#### Ejecutar todas las pruebas

**Windows:**

```powershell
dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx --logger "console;verbosity=normal"
```

**macOS:**

```bash
dotnet test ./01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.slnx --logger "console;verbosity=normal"
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

**Windows:**

```powershell
$env:SELENIUM_HEADLESS = "true"

dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
```

**macOS:**

```bash
$env:SELENIUM_HEADLESS = "true"

dotnet test ./01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.slnx
```

La variable `SELENIUM_HEADLESS` afecta a los navegadores habilitados.

Para volver a la configuración predeterminada:

**Windows y macOS (PowerShell):**

```powershell
Remove-Item Env:SELENIUM_BROWSER -ErrorAction SilentlyContinue
Remove-Item Env:SELENIUM_HEADLESS -ErrorAction SilentlyContinue
Remove-Item Env:SELENIUM_TIMEOUT -ErrorAction SilentlyContinue
Remove-Item Env:SELENIUM_BASE_URL -ErrorAction SilentlyContinue
```

#### Resultados Allure

Los resultados de las pruebas se generan en:

```text
01_Automatizacion_Web_Selenium_CSharp/
└── SeleniumAutomation.Tests/
    └── TestResults/
        └── AllureResults/
```

Para generar un informe independiente de Selenium:

**Windows:**

```powershell
allure generate .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.Tests\TestResults\AllureResults --clean -o .\01_Automatizacion_Web_Selenium_CSharp\reports\allure-report
```

**macOS:**

```bash
allure generate ./01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.Tests/TestResults/AllureResults --clean -o ./01_Automatizacion_Web_Selenium_CSharp/reports/allure-report
```

Abrir el informe:

```powershell
allure open .\01_Automatizacion_Web_Selenium_CSharp\reports\allure-report
```

En macOS también se puede utilizar:

```bash
allure open ./01_Automatizacion_Web_Selenium_CSharp/reports/allure-report
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

```text
SeleniumAutomation.Tests/bin/Debug/net10.0/TestResults/Screenshots/
```

Esta ubicación corresponde al directorio de trabajo utilizado actualmente por NUnit durante la ejecución.

---

### Proyecto 02 - Playwright + Python

**Tecnologías:**
- Python
- Playwright
- Pytest
- Page Object Model

#### Ejecutar todas las pruebas manualmente

Desde la raíz del repositorio:

**Windows:**

```powershell
.\02_Automatizacion_Web_Playwright_Python\.venv\Scripts\python.exe -m pytest .\02_Automatizacion_Web_Playwright_Python\tests -v
```

**macOS:**

```bash
./02_Automatizacion_Web_Playwright_Python/.venv/bin/python -m pytest ./02_Automatizacion_Web_Playwright_Python/tests -v
```

#### Ejecutar el script automatizado

El proyecto dispone de un script propio que ejecuta los tests y genera un dashboard HTML.

**Windows:**

```powershell
.\02_Automatizacion_Web_Playwright_Python\run_tests.ps1
```

**macOS:**

```bash
pwsh ./02_Automatizacion_Web_Playwright_Python/run_tests.ps1
```

El script genera:

- `results.json`
- `report.html`

Ubicación de los informes:

```text
02_Automatizacion_Web_Playwright_Python/reports/
```

El dashboard HTML se abre automáticamente al finalizar la ejecución.

---

### Proyecto 03 - Playwright + .NET

**Tecnologías:**
- C#
- .NET 10
- Playwright
- NUnit

#### Compilar

**Windows:**

```powershell
dotnet build .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx
```

**macOS:**

```bash
dotnet build ./03_Automatizacion_Web_Playwright_DotNet/QAAutomationFramework.slnx
```

#### Ejecutar pruebas

**Windows:**

```powershell
dotnet test .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx
```

**macOS:**

```bash
dotnet test ./03_Automatizacion_Web_Playwright_DotNet/QAAutomationFramework.slnx
```

Los resultados de la ejecución se muestran en la consola.

---

### Proyecto 04 - API Automation + Python

**Tecnologías:**
- Python
- Requests
- Pytest
- JSON Schema
- Allure
- HTML Reporting

#### Ejecutar todas las pruebas

**Windows:**

```powershell
.\04_Automatizacion_API_Python_Requests_Pytest\.venv\Scripts\python.exe -m pytest .\04_Automatizacion_API_Python_Requests_Pytest\tests -v
```

**macOS:**

```bash
./04_Automatizacion_API_Python_Requests_Pytest/.venv/bin/python -m pytest ./04_Automatizacion_API_Python_Requests_Pytest/tests -v
```

El proyecto genera automáticamente:

- Resultados Allure.
- Informe HTML de Pytest.

Ubicación de los resultados:

```text
04_Automatizacion_API_Python_Requests_Pytest/
├── allure-results/
└── reports/
    └── api_test_report.html
```

#### Visualizar informe Allure independiente

```powershell
allure serve .\04_Automatizacion_API_Python_Requests_Pytest\allure-results
```

En macOS:

```bash
allure serve ./04_Automatizacion_API_Python_Requests_Pytest/allure-results
```

Este comando inicia un servidor local y permite consultar el informe en el navegador.

---

## 4. Ejecutar pruebas específicas

Los siguientes ejemplos utilizan el proyecto de API, pero se pueden adaptar a cualquier proyecto Python.

### Ejecutar un único archivo de tests

**Windows:**

```powershell
.\04_Automatizacion_API_Python_Requests_Pytest\.venv\Scripts\python.exe -m pytest .\04_Automatizacion_API_Python_Requests_Pytest\tests\test_users.py -v
```

**macOS:**

```bash
./04_Automatizacion_API_Python_Requests_Pytest/.venv/bin/python -m pytest ./04_Automatizacion_API_Python_Requests_Pytest/tests/test_users.py -v
```

### Ejecutar un test concreto

```powershell
python -m pytest RUTA_DEL_ARCHIVO -k "get_user" -v
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
| 02 Playwright Python | `reports/report.html` + `results.json` |
| 03 Playwright .NET | Resultados en consola |
| 04 API Python | `reports/api_test_report.html` + resultados Allure |

### Informe Allure conjunto

El ejecutor central recopila los resultados de Selenium y API en una única carpeta:

```text
allure-results/
```

El informe HTML conjunto se genera en:

```text
allure-report/
```

Para abrirlo:

```powershell
allure open allure-report
```

Para volver a generarlo manualmente a partir de los resultados recopilados:

```powershell
allure generate allure-results --clean -o allure-report
```

**Importante:** el ejecutor central limpia los resultados anteriores de Selenium y los resultados conjuntos antes de cada ejecución. Por tanto, conviene ejecutar de nuevo los proyectos antes de generar un informe actualizado.

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

**Windows:**

```powershell
.\02_Automatizacion_Web_Playwright_Python\.venv\Scripts\python.exe -m pip install -r .\02_Automatizacion_Web_Playwright_Python\requirements.txt
```

**macOS:**

```bash
./02_Automatizacion_Web_Playwright_Python/.venv/bin/python -m pip install -r ./02_Automatizacion_Web_Playwright_Python/requirements.txt
```

### Instalar dependencias del proyecto 04

**Windows:**

```powershell
.\04_Automatizacion_API_Python_Requests_Pytest\.venv\Scripts\python.exe -m pip install -r .\04_Automatizacion_API_Python_Requests_Pytest\requirements.txt
```

**macOS:**

```bash
./04_Automatizacion_API_Python_Requests_Pytest/.venv/bin/python -m pip install -r ./04_Automatizacion_API_Python_Requests_Pytest/requirements.txt
```

### Restaurar dependencias .NET

```powershell
dotnet restore .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
dotnet restore .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx
```

### Comprobar proyectos .NET

```powershell
dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx
dotnet test .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx
```

---

## 7. Tabla resumen de comandos principales

| Objetivo | Windows | macOS |
|---|---|---|
| Ejecutar todos los proyectos | `.\run_all_tests.ps1` | `pwsh ./run_all_tests.ps1` |
| Selenium C# | `dotnet test .\01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx` | `dotnet test ./01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.slnx` |
| Playwright Python | `.\02_Automatizacion_Web_Playwright_Python\run_tests.ps1` | `pwsh ./02_Automatizacion_Web_Playwright_Python/run_tests.ps1` |
| Playwright .NET | `dotnet test .\03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx` | `dotnet test ./03_Automatizacion_Web_Playwright_DotNet/QAAutomationFramework.slnx` |
| API Python | `.\04_Automatizacion_API_Python_Requests_Pytest\.venv\Scripts\python.exe -m pytest .\04_Automatizacion_API_Python_Requests_Pytest\tests -v` | `./04_Automatizacion_API_Python_Requests_Pytest/.venv/bin/python -m pytest ./04_Automatizacion_API_Python_Requests_Pytest/tests -v` |
| Abrir informe Allure conjunto | `allure open allure-report` | `allure open allure-report` |

---

## 8. Buenas prácticas

- Ejecutar los comandos desde la raíz del portfolio, salvo que se indique lo contrario.
- Utilizar el entorno virtual `.venv` correspondiente a cada proyecto Python.
- Mantener actualizadas las dependencias de cada proyecto.
- Comprobar las versiones de .NET, Python, PowerShell y Allure cuando se configure un equipo nuevo.
- Revisar los informes HTML después de cada ejecución.
- Ejecutar el script central para obtener una validación general del portfolio.
- No publicar credenciales ni información confidencial.
- Mantener actualizada esta guía cuando se incorporen nuevos proyectos.

---

**Senior QA Automation Portfolio**

Documento de referencia para la ejecución y mantenimiento de los proyectos en Windows y macOS.
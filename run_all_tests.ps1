# ============================================================
# SENIOR QA AUTOMATION PORTFOLIO
# EJECUTOR CENTRAL DE TODOS LOS PROYECTOS
# Compatible con Windows y macOS
# ============================================================

$ErrorActionPreference = "Continue"

$root = $PSScriptRoot
Set-Location $root

$esWindows = $env:OS -eq "Windows_NT"

# ------------------------------------------------------------
# CONFIGURACION DE RUTAS
# ------------------------------------------------------------

if ($esWindows) {
    $pythonPlaywright = Join-Path $root "02_Automatizacion_Web_Playwright_Python/.venv/Scripts/python.exe"
    $pythonApi = Join-Path $root "04_Automatizacion_API_Python_Requests_Pytest/.venv/Scripts/python.exe"
    $powerShellCommand = "powershell.exe"
}
else {
    $pythonPlaywright = Join-Path $root "02_Automatizacion_Web_Playwright_Python/.venv/bin/python"
    $pythonApi = Join-Path $root "04_Automatizacion_API_Python_Requests_Pytest/.venv/bin/python"
    $powerShellCommand = "pwsh"
}

# Rutas de resultados Allure
$seleniumAllureResults = Join-Path $root "01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.Tests/TestResults/AllureResults"
$apiAllureResults = Join-Path $root "04_Automatizacion_API_Python_Requests_Pytest/allure-results"

$allureResults = Join-Path $root "allure-results"
$allureReport = Join-Path $root "allure-report"

$results = @()

# ------------------------------------------------------------
# FUNCION PARA EJECUTAR CADA PROYECTO
# ------------------------------------------------------------

function Invoke-Project {
    param(
        [string]$Name,
        [string]$Command,
        [string[]]$Arguments
    )

    Write-Host "`n============================================" -ForegroundColor Cyan
    Write-Host "PROYECTO: $Name" -ForegroundColor Yellow
    Write-Host "============================================"

    $exitCode = 1

    try {
        & $Command @Arguments
        $exitCode = $LASTEXITCODE

        if ($null -eq $exitCode) {
            $exitCode = 0
        }
    }
    catch {
        Write-Host "ERROR: $_" -ForegroundColor Red
        $exitCode = 1
    }

    if ($exitCode -eq 0) {
        Write-Host "`nRESULTADO: CORRECTO" -ForegroundColor Green

        $script:results += [PSCustomObject]@{
            Proyecto = $Name
            Estado = "CORRECTO"
        }
    }
    else {
        Write-Host "`nRESULTADO: ERROR" -ForegroundColor Red

        $script:results += [PSCustomObject]@{
            Proyecto = $Name
            Estado = "ERROR"
        }
    }
}

# ------------------------------------------------------------
# COMPROBACIONES INICIALES
# ------------------------------------------------------------

Write-Host "`nSENIOR QA AUTOMATION PORTFOLIO" -ForegroundColor Cyan
Write-Host "Sistema operativo: $(if ($esWindows) { 'Windows' } else { 'macOS / Linux' })"
Write-Host "Iniciando ejecucion de los proyectos..." -ForegroundColor Cyan

if (-not (Get-Command dotnet -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: No se encuentra .NET." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $pythonPlaywright)) {
    Write-Host "ERROR: No se encuentra Python de Playwright." -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $pythonApi)) {
    Write-Host "ERROR: No se encuentra Python de API." -ForegroundColor Red
    exit 1
}

# ------------------------------------------------------------
# PREPARAR RESULTADOS ALLURE
# ------------------------------------------------------------

Write-Host "`nPREPARANDO RESULTADOS ALLURE..." -ForegroundColor Cyan

# Limpiar resultados anteriores de Selenium
if (Test-Path $seleniumAllureResults) {
    Get-ChildItem -Path $seleniumAllureResults -Force |
        Remove-Item -Recurse -Force
}
else {
    New-Item -ItemType Directory -Path $seleniumAllureResults -Force | Out-Null
}

# Limpiar resultados centrales anteriores
if (Test-Path $allureResults) {
    Remove-Item -Path $allureResults -Recurse -Force
}

New-Item -ItemType Directory -Path $allureResults -Force | Out-Null

Write-Host "Carpetas Allure preparadas." -ForegroundColor Green

# ------------------------------------------------------------
# 01 - SELENIUM C#
# ------------------------------------------------------------

Invoke-Project `
    -Name "01 - Selenium WebDriver + C#" `
    -Command "dotnet" `
    -Arguments @(
        "test",
        (Join-Path $root "01_Automatizacion_Web_Selenium_CSharp/SeleniumAutomation.slnx")
    )

# ------------------------------------------------------------
# 02 - PLAYWRIGHT PYTHON
# ------------------------------------------------------------

Invoke-Project `
    -Name "02 - Playwright + Python" `
    -Command $powerShellCommand `
    -Arguments @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File",
        (Join-Path $root "02_Automatizacion_Web_Playwright_Python/run_tests.ps1")
    )

# ------------------------------------------------------------
# 03 - PLAYWRIGHT .NET
# ------------------------------------------------------------

Invoke-Project `
    -Name "03 - Playwright + .NET" `
    -Command "dotnet" `
    -Arguments @(
        "test",
        (Join-Path $root "03_Automatizacion_Web_Playwright_DotNet/QAAutomationFramework.slnx")
    )

# ------------------------------------------------------------
# 04 - API AUTOMATION PYTHON
# ------------------------------------------------------------

$apiProject = Join-Path $root "04_Automatizacion_API_Python_Requests_Pytest"

Invoke-Project `
    -Name "04 - API Automation + Python" `
    -Command $pythonApi `
    -Arguments @(
        "-m", "pytest",
        (Join-Path $apiProject "tests"),
        "-v"
    )

# ------------------------------------------------------------
# RECOPILAR Y GENERAR INFORME ALLURE
# ------------------------------------------------------------

Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "GENERANDO INFORME ALLURE" -ForegroundColor Cyan
Write-Host "============================================"

$allureSources = @(
    $seleniumAllureResults,
    $apiAllureResults
)

foreach ($source in $allureSources) {
    if (Test-Path $source) {
        Get-ChildItem -Path $source -Force |
            Copy-Item -Destination $allureResults -Recurse -Force

        Write-Host "Resultados recopilados: $source" -ForegroundColor Green
    }
    else {
        Write-Host "AVISO: No existe la carpeta $source" -ForegroundColor Yellow
    }
}

$allureCommand = Get-Command allure -ErrorAction SilentlyContinue

if ($null -eq $allureCommand) {
    Write-Host "AVISO: Allure CLI no está instalado o no está en PATH." -ForegroundColor Yellow
    Write-Host "Los tests han terminado, pero no se ha generado el informe Allure."
}
else {
    $allureResultFiles = @(
        Get-ChildItem -Path $allureResults -Filter "*-result.json" -File -ErrorAction SilentlyContinue
    )

    if ($allureResultFiles.Count -gt 0) {
        Write-Host "Tests encontrados en Allure: $($allureResultFiles.Count)" -ForegroundColor Cyan

        & $allureCommand.Source generate $allureResults --clean -o $allureReport
        $allureExitCode = $LASTEXITCODE

        if ($allureExitCode -eq 0 -and (Test-Path $allureReport)) {
            Write-Host "Informe Allure generado correctamente." -ForegroundColor Green
            Write-Host "Ubicacion: $allureReport"

            try {
                Start-Process -FilePath $allureCommand.Source -ArgumentList @("open", $allureReport)
                Write-Host "Abriendo informe Allure..." -ForegroundColor Green
            }
            catch {
                Write-Host "No se pudo abrir automaticamente el informe: $_" -ForegroundColor Yellow
                Write-Host "Puedes abrirlo manualmente con: allure open allure-report"
            }
        }
        else {
            Write-Host "ERROR: No se pudo generar el informe Allure." -ForegroundColor Red
        }
    }
    else {
        Write-Host "AVISO: No se encontraron resultados Allure para generar el informe." -ForegroundColor Yellow
    }
}

# ------------------------------------------------------------
# RESUMEN FINAL
# ------------------------------------------------------------

Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "RESUMEN GENERAL DEL PORTFOLIO" -ForegroundColor Cyan
Write-Host "============================================"

$results | Format-Table -AutoSize

$correctos = @($results | Where-Object Estado -eq "CORRECTO").Count
$errores = @($results | Where-Object Estado -eq "ERROR").Count

Write-Host "Proyectos correctos: $correctos" -ForegroundColor Green
Write-Host "Proyectos con errores: $errores" -ForegroundColor Red

if ($errores -gt 0) {
    Write-Host "`nATENCION: HAY PROYECTOS CON ERRORES." -ForegroundColor Red
    exit 1
}

Write-Host "`nTODOS LOS PROYECTOS HAN FINALIZADO CORRECTAMENTE." -ForegroundColor Green

exit 0

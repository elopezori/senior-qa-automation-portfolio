# ============================================================
# SENIOR QA AUTOMATION PORTFOLIO
# EJECUTOR CENTRAL DE TODOS LOS PROYECTOS
# ============================================================

$ErrorActionPreference = "Continue"

# Directorio raiz del portfolio
$root = $PSScriptRoot

# Activar entorno virtual del portfolio
$python = Join-Path $root "venv\Scripts\python.exe"

$results = @()

function Invoke-Project {
    param(
        [string]$Name,
        [string]$Command,
        [string[]]$Arguments
    )

    Write-Host "`n============================================" -ForegroundColor Cyan
    Write-Host "PROYECTO: $Name" -ForegroundColor Yellow
    Write-Host "============================================"

    & $Command @Arguments

    $exitCode = $LASTEXITCODE

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
# COMPROBAR PYTHON
# ------------------------------------------------------------

if (-not (Test-Path $python)) {
    Write-Host "ERROR: No se encuentra el entorno virtual." -ForegroundColor Red
    exit 1
}

Write-Host "`nSENIOR QA AUTOMATION PORTFOLIO" -ForegroundColor Cyan
Write-Host "Iniciando ejecucion de los proyectos..." -ForegroundColor Cyan

# ------------------------------------------------------------
# 01 - SELENIUM C#
# ------------------------------------------------------------

Invoke-Project `
    -Name "01 - Selenium WebDriver + C#" `
    -Command "dotnet" `
    -Arguments @(
        "test",
        (Join-Path $root "01_Automatizacion_Web_Selenium_CSharp\SeleniumAutomation.slnx")
    )

# ------------------------------------------------------------
# 02 - PLAYWRIGHT PYTHON
# ------------------------------------------------------------

Invoke-Project `
    -Name "02 - Playwright + Python" `
    -Command "powershell.exe" `
    -Arguments @(
        "-NoProfile",
        "-ExecutionPolicy", "RemoteSigned",
        "-File",
        (Join-Path $root "02_Automatizacion_Web_Playwright_Python\run_tests.ps1")
    )

# ------------------------------------------------------------
# 03 - PLAYWRIGHT .NET
# ------------------------------------------------------------

Invoke-Project `
    -Name "03 - Playwright + .NET" `
    -Command "dotnet" `
    -Arguments @(
        "test",
        (Join-Path $root "03_Automatizacion_Web_Playwright_DotNet\QAAutomationFramework.slnx")
    )

# ------------------------------------------------------------
# 04 - API AUTOMATION PYTHON
# ------------------------------------------------------------

$apiProject = Join-Path $root "04_Automatizacion_API_Python_Requests_Pytest"

Invoke-Project `
    -Name "04 - API Automation + Python" `
    -Command $python `
    -Arguments @(
        "-m", "pytest",
        $apiProject,
        "-v"
    )

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
    exit 1
}

Write-Host "`nTODOS LOS PROYECTOS HAN FINALIZADO CORRECTAMENTE." -ForegroundColor Green

exit 0
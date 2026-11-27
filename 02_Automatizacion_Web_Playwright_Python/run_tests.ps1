# ============================================================
# QA AUTOMATION - PLAYWRIGHT PYTHON TEST RUNNER
# Compatible con Windows y macOS
# ============================================================

$ErrorActionPreference = "Continue"

Set-Location $PSScriptRoot

$reportsDir = Join-Path $PSScriptRoot "reports"
$jsonFile = Join-Path $reportsDir "results.json"
$htmlFile = Join-Path $reportsDir "report.html"
$reportScript = Join-Path $PSScriptRoot "reporting/generate_report.py"

# ------------------------------------------------------------
# 1. DETECTAR PYTHON
# ------------------------------------------------------------

if ($env:OS -eq "Windows_NT") {
    $python = Join-Path $PSScriptRoot ".venv/Scripts/python.exe"
}
else {
    $python = Join-Path $PSScriptRoot ".venv/bin/python"
}

if (-not (Test-Path $python)) {
    if ($env:OS -eq "Windows_NT") {
        $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    }
    else {
        $pythonCommand = Get-Command python3 -ErrorAction SilentlyContinue
    }

    if ($null -eq $pythonCommand) {
        Write-Host "ERROR: No se encuentra Python." -ForegroundColor Red
        exit 1
    }

    $python = $pythonCommand.Source
}

Write-Host "`n===================================="
Write-Host "QA AUTOMATION - PLAYWRIGHT"
Write-Host "===================================="

& $python --version

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: No se pudo ejecutar Python." -ForegroundColor Red
    exit 1
}

# ------------------------------------------------------------
# 2. COMPROBAR PYTEST
# ------------------------------------------------------------

& $python -m pytest --version

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Pytest no está instalado." -ForegroundColor Red
    exit 1
}

# ------------------------------------------------------------
# 3. PREPARAR INFORMES
# ------------------------------------------------------------

New-Item -ItemType Directory -Path $reportsDir -Force | Out-Null

if (Test-Path $jsonFile) {
    Remove-Item $jsonFile -Force
}

# ------------------------------------------------------------
# 4. EJECUTAR TESTS
# ------------------------------------------------------------

Write-Host "`nINICIANDO TESTS DE PLAYWRIGHT..." -ForegroundColor Cyan

$testsDir = Join-Path $PSScriptRoot "tests"

& $python -m pytest $testsDir -v -s --json-report "--json-report-file=$jsonFile"

$pytestExitCode = $LASTEXITCODE

# ------------------------------------------------------------
# 5. GENERAR DASHBOARD HTML
# ------------------------------------------------------------

if (Test-Path $jsonFile) {

    Write-Host "`nGENERANDO DASHBOARD HTML..." -ForegroundColor Cyan

    & $python $reportScript
    $reportExitCode = $LASTEXITCODE

    if ($reportExitCode -ne 0) {
        Write-Host "ERROR: No se pudo generar el dashboard." -ForegroundColor Red
        exit $reportExitCode
    }

    # --------------------------------------------------------
    # 6. ABRIR INFORME
    # --------------------------------------------------------

    if (Test-Path $htmlFile) {

        Write-Host "Dashboard generado correctamente." -ForegroundColor Green

        if ($env:OS -eq "Windows_NT") {
            Start-Process -FilePath $htmlFile
        }
        elseif ($IsMacOS) {
            & open $htmlFile
        }
        elseif ($IsLinux) {
            & xdg-open $htmlFile
        }

    }
    else {
        Write-Host "ERROR: No se encuentra report.html." -ForegroundColor Red
        exit 1
    }

}
else {
    Write-Host "ERROR: No se ha generado results.json." -ForegroundColor Red
    exit 1
}

# ------------------------------------------------------------
# 7. RESULTADO FINAL
# ------------------------------------------------------------

if ($pytestExitCode -eq 0) {
    Write-Host "`nTODOS LOS TESTS HAN FINALIZADO CORRECTAMENTE." -ForegroundColor Green
}
else {
    Write-Host "`nATENCION: ALGUNOS TESTS HAN FALLADO." -ForegroundColor Red
}

exit $pytestExitCode

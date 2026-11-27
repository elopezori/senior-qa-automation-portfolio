
# ============================================================
# QA AUTOMATION - PLAYWRIGHT TEST RUNNER
# Ejecucion de Pytest y generacion del dashboard HTML
# ============================================================

# 1. CONFIGURACION DE RUTAS

Set-Location $PSScriptRoot

$reportsDir = Join-Path $PSScriptRoot "reports"
$jsonFile = Join-Path $reportsDir "results.json"
$htmlFile = Join-Path $reportsDir "report.html"
$reportScript = Join-Path $PSScriptRoot "reporting\generate_report.py"


# 2. COMPROBAR PYTHON

Write-Host "`n===================================="
Write-Host "QA AUTOMATION - PLAYWRIGHT"
Write-Host "====================================`n"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: Python no esta instalado o no esta disponible en PATH."
    exit 1
}

python --version

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: No se pudo ejecutar Python."
    exit 1
}


# 3. COMPROBAR PYTEST

Write-Host "`nComprobando Pytest..."

python -m pytest --version

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Pytest no esta instalado."
    Write-Host "Ejecuta: python -m pip install -r requirements.txt"
    exit 1
}


# 4. PREPARAR CARPETA DE INFORMES

New-Item -ItemType Directory -Path $reportsDir -Force | Out-Null

# Eliminar resultados anteriores para evitar generar
# un dashboard con datos de una ejecucion antigua.

if (Test-Path $jsonFile) {
    Remove-Item $jsonFile -Force
}


# 5. EJECUTAR TESTS

Write-Host "`n===================================="
Write-Host "INICIANDO TESTS DE PLAYWRIGHT"
Write-Host "====================================`n"

python -m pytest .\tests -v -s --json-report --json-report-file=$jsonFile

$pytestExitCode = $LASTEXITCODE


# 6. GENERAR DASHBOARD

if (Test-Path $jsonFile) {

    Write-Host "`n===================================="
    Write-Host "GENERANDO DASHBOARD HTML"
    Write-Host "====================================`n"

    python $reportScript

    $reportExitCode = $LASTEXITCODE

    if ($reportExitCode -ne 0) {
        Write-Host "`nERROR: No se pudo generar el dashboard."
        exit $reportExitCode
    }

    # 7. ABRIR DASHBOARD

    if (Test-Path $htmlFile) {

        Write-Host "`nDashboard generado correctamente."
        Write-Host "Abriendo informe HTML..."

        Start-Process -FilePath $htmlFile

    }
    else {
        Write-Host "ERROR: No se encuentra el archivo report.html."
        exit 1
    }

}
else {

    Write-Host "`nERROR: No se ha generado results.json."

    if ($pytestExitCode -ne 0) {
        exit $pytestExitCode
    }

    exit 1
}


# 8. RESULTADO FINAL

Write-Host "`n===================================="

if ($pytestExitCode -eq 0) {

    Write-Host "TODOS LOS TESTS HAN FINALIZADO CORRECTAMENTE."

}
else {

    Write-Host "ATENCION: ALGUNOS TESTS HAN FALLADO."
    Write-Host "Consulta el dashboard para ver los resultados."

}

Write-Host "====================================`n"

exit $pytestExitCode
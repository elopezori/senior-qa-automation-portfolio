Set-Location $PSScriptRoot

Write-Host "`n===================================="
Write-Host "INICIANDO TESTS DE PLAYWRIGHT"
Write-Host "====================================`n"

New-Item -ItemType Directory -Path ".\reports" -Force | Out-Null

python -m pytest .\tests -v -s --json-report --json-report-file=reports/results.json
$pytestExitCode = $LASTEXITCODE

if (Test-Path ".\reports\results.json") {
    Write-Host "`n===================================="
    Write-Host "GENERANDO DASHBOARD"
    Write-Host "====================================`n"

    python .\reporting\generate_report.py
    $reportExitCode = $LASTEXITCODE

    if ($reportExitCode -eq 0) {
        Start-Process ".\reports\report.html"
    }
    else {
        Write-Host "ERROR: No se pudo generar el dashboard."
        exit $reportExitCode
    }
}
else {
    Write-Host "ERROR: No se ha generado el archivo JSON."
    exit 1
}

if ($pytestExitCode -ne 0) {
    Write-Host "`nATENCION: Hay tests que no han pasado."
    exit $pytestExitCode
}

Write-Host "`nPROCESO COMPLETADO CORRECTAMENTE."
exit 0

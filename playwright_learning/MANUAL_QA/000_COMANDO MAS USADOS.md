# COMANDOS MAS USADOS - QA AUTOMATION

## 1. Activar el entorno virtual
.\venv\Scripts\Activate.ps1

## 2. Ejecutar todos los tests y generar el dashboard automaticamente
.\run_tests.ps1

## 3. Ejecutar los tests directamente con Pytest
python -m pytest .\tests -v -s

## 4. Generar el JSON de resultados
python -m pytest .\tests -v -s --json-report --json-report-file=reports/results.json

## 5. Generar el dashboard HTML a partir del JSON
python .\reporting\generate_report.py

## 6. Abrir el dashboard
Start-Process .\reports\report.html

## 7. Consultar las dependencias instaladas
python -m pip freeze

## 8. Instalar las dependencias del proyecto
python -m pip install -r requirements.txt

## 9. Instalar Chromium para Playwright
python -m playwright install chromium

## 10. Consultar el estado de Git
git status

## 11. Consultar la configuracion del repositorio remoto
git remote -v


import json
import html
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

JSON_FILE = BASE_DIR / "reports" / "results.json"
HTML_FILE = BASE_DIR / "reports" / "report.html"

# Cargar resultados de Pytest
with open(JSON_FILE, "r", encoding="utf-8") as file:
    report = json.load(file)

tests = report.get("tests", [])

# Obtener información de cada test
def get_outcome(test):
    return test.get("outcome", "unknown").lower()


def get_duration(test, phase):
    return float(test.get(phase, {}).get("duration", 0))


def get_total_duration(test):
    # Pytest guarda el tiempo por fase.
    # La suma evita depender de un campo duration inexistente.
    return sum(
        get_duration(test, phase)
        for phase in ("setup", "call", "teardown")
    )


passed = sum(get_outcome(t) == "passed" for t in tests)
failed = sum(get_outcome(t) == "failed" for t in tests)
skipped = sum(get_outcome(t) == "skipped" for t in tests)
errors = sum(get_outcome(t) == "error" for t in tests)

total = len(tests)
pass_rate = round((passed / total) * 100, 1) if total else 0

total_duration = sum(get_total_duration(t) for t in tests)

max_duration = max(
    (get_total_duration(t) for t in tests),
    default=1
) or 1


# Construir filas de la tabla
rows = ""

for test in tests:
    nodeid = html.escape(test.get("nodeid", "Unknown test"))
    outcome = get_outcome(test)
    total_time = get_total_duration(test)

    setup_time = get_duration(test, "setup")
    call_time = get_duration(test, "call")
    teardown_time = get_duration(test, "teardown")

    status_class = outcome if outcome in (
        "passed", "failed", "skipped", "error"
    ) else "unknown"

    # Obtener mensajes de error disponibles
    error_details = []

    for phase in ("setup", "call", "teardown"):
        phase_data = test.get(phase, {})
        crash = phase_data.get("crash", {})

        message = crash.get("message")

        if message:
            error_details.append(
                f"{phase.upper()}: {message}"
            )

    error_html = ""

    if error_details:
        error_text = html.escape("\n".join(error_details))
        error_html = f"""
        <details class="error-details">
            <summary>Ver error</summary>
            <pre>{error_text}</pre>
        </details>
        """

    rows += f"""
    <tr>
        <td>
            <span class="status {status_class}">
                {html.escape(outcome.upper())}
            </span>
        </td>
        <td class="test-name">
            {nodeid}
            {error_html}
        </td>
        <td>{setup_time:.2f} s</td>
        <td>{call_time:.2f} s</td>
        <td>{teardown_time:.2f} s</td>
        <td><strong>{total_time:.2f} s</strong></td>
    </tr>
    """


# Construir gráficas de duración
bars = ""

for test in tests:
    name = html.escape(test.get("nodeid", "Unknown test"))
    seconds = get_total_duration(test)

    width = seconds / max_duration * 100
    outcome = get_outcome(test)

    color = (
        "#34d399"
        if outcome == "passed"
        else "#f87171"
        if outcome in ("failed", "error")
        else "#fbbf24"
    )

    bars += f"""
    <div class="bar-item">
        <div class="bar-label">
            <span>{name}</span>
            <strong>{seconds:.2f} s</strong>
        </div>
        <div class="bar-track">
            <div class="bar-fill"
                 style="width:{width}%;background:{color}">
            </div>
        </div>
    </div>
    """


generated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

html_content = f"""
<!DOCTYPE html>
<html lang="es">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>QA Automation Dashboard</title>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 30px;
    background: #080d17;
    color: #e5e7eb;
    font-family: Arial, Helvetica, sans-serif;
}}

.container {{
    max-width: 1400px;
    margin: auto;
}}

header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    flex-wrap: wrap;
    gap: 15px;
}}

h1 {{
    margin: 0;
    font-size: 29px;
    color: #fff;
}}

.subtitle {{
    color: #94a3b8;
    margin-top: 8px;
    font-size: 13px;
}}

.badge {{
    background: #123b30;
    color: #34d399;
    padding: 10px 15px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: bold;
}}

.cards {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 16px;
    margin-bottom: 22px;
}}

.card, .panel {{
    background: #111a2a;
    border: 1px solid #263449;
    border-radius: 13px;
    padding: 22px;
}}

.card span {{
    color: #94a3b8;
    font-size: 12px;
}}

.card h2 {{
    font-size: 30px;
    margin: 12px 0 0;
}}

.green {{ color: #34d399; }}
.red {{ color: #f87171; }}
.yellow {{ color: #fbbf24; }}
.blue {{ color: #38bdf8; }}

.panels {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 22px;
}}

h3 {{
    margin-top: 0;
    color: #f8fafc;
    font-size: 17px;
}}

.chart {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 30px;
    min-height: 190px;
    flex-wrap: wrap;
}}

.donut {{
    width: 155px;
    height: 155px;
    border-radius: 50%;
    background: conic-gradient(
        #34d399 0% {pass_rate}%,
        #f87171 {pass_rate}% 100%
    );
    display: flex;
    align-items: center;
    justify-content: center;
}}

.donut-inner {{
    width: 115px;
    height: 115px;
    border-radius: 50%;
    background: #111a2a;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}}

.donut-inner strong {{
    font-size: 27px;
    color: #fff;
}}

.donut-inner small {{
    color: #94a3b8;
}}

.legend {{
    line-height: 2.2;
    color: #cbd5e1;
    font-size: 13px;
}}

.dot {{
    display: inline-block;
    width: 9px;
    height: 9px;
    border-radius: 50%;
    margin-right: 8px;
}}

.bar-item {{
    margin: 17px 0;
}}

.bar-label {{
    display: flex;
    justify-content: space-between;
    gap: 10px;
    font-size: 12px;
    margin-bottom: 8px;
    color: #cbd5e1;
}}

.bar-label span {{
    overflow-wrap: anywhere;
}}

.bar-track {{
    height: 9px;
    background: #263449;
    border-radius: 10px;
    overflow: hidden;
}}

.bar-fill {{
    height: 100%;
    border-radius: 10px;
}}

.table-container {{
    overflow-x: auto;
}}

table {{
    width: 100%;
    min-width: 850px;
    border-collapse: collapse;
    font-size: 13px;
}}

th {{
    text-align: left;
    color: #94a3b8;
    padding: 14px;
    border-bottom: 1px solid #263449;
    white-space: nowrap;
}}

td {{
    padding: 15px 14px;
    border-bottom: 1px solid #263449;
    white-space: nowrap;
}}

.test-name {{
    white-space: normal;
    min-width: 280px;
    overflow-wrap: anywhere;
}}

.status {{
    padding: 6px 10px;
    border-radius: 15px;
    font-size: 10px;
    font-weight: bold;
}}

.status.passed {{
    background: #123b30;
    color: #34d399;
}}

.status.failed, .status.error {{
    background: #451f28;
    color: #f87171;
}}

.status.skipped {{
    background: #44351b;
    color: #fbbf24;
}}

.error-details {{
    margin-top: 10px;
    color: #f87171;
    font-size: 12px;
}}

.error-details summary {{
    cursor: pointer;
}}

.error-details pre {{
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    background: #080d17;
    padding: 12px;
    border-radius: 8px;
}}

footer {{
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 25px;
}}

@media(max-width: 1000px) {{
    .cards {{
        grid-template-columns: repeat(3, 1fr);
    }}
}}

@media(max-width: 750px) {{
    body {{
        padding: 15px;
    }}

    .cards {{
        grid-template-columns: repeat(2, 1fr);
    }}

    .panels {{
        grid-template-columns: 1fr;
    }}
}}

</style>
</head>

<body>

<div class="container">

<header>
    <div>
        <h1>QA AUTOMATION DASHBOARD</h1>
        <div class="subtitle">
            PLAYWRIGHT · PYTEST · TEST EXECUTION REPORT
        </div>
    </div>

    <div class="badge">● EXECUTION COMPLETED</div>
</header>


<section class="cards">

    <div class="card">
        <span>TOTAL TESTS</span>
        <h2>{total}</h2>
    </div>

    <div class="card">
        <span>PASSED</span>
        <h2 class="green">{passed}</h2>
    </div>

    <div class="card">
        <span>FAILED / ERRORS</span>
        <h2 class="red">{failed + errors}</h2>
    </div>

    <div class="card">
        <span>PASS RATE</span>
        <h2 class="green">{pass_rate}%</h2>
    </div>

    <div class="card">
        <span>TOTAL DURATION</span>
        <h2 class="blue">{total_duration:.2f} s</h2>
    </div>

</section>


<section class="panels">

    <div class="panel">
        <h3>Test results distribution</h3>

        <div class="chart">

            <div class="donut">
                <div class="donut-inner">
                    <strong>{pass_rate}%</strong>
                    <small>PASS RATE</small>
                </div>
            </div>

            <div class="legend">
                <div>
                    <span class="dot" style="background:#34d399"></span>
                    Passed: {passed}
                </div>

                <div>
                    <span class="dot" style="background:#f87171"></span>
                    Failed: {failed}
                </div>

                <div>
                    <span class="dot" style="background:#fbbf24"></span>
                    Skipped: {skipped}
                </div>

                <div>
                    <span class="dot" style="background:#a78bfa"></span>
                    Errors: {errors}
                </div>
            </div>

        </div>
    </div>


    <div class="panel">
        <h3>Test execution duration</h3>
        {bars if bars else '<p>No test data available.</p>'}
    </div>

</section>


<section class="panel">

    <h3>Detailed test results</h3>

    <div class="table-container">

        <table>

            <thead>
                <tr>
                    <th>STATUS</th>
                    <th>TEST NAME</th>
                    <th>SETUP</th>
                    <th>CALL</th>
                    <th>TEARDOWN</th>
                    <th>TOTAL TIME</th>
                </tr>
            </thead>

            <tbody>
                {rows if rows else '<tr><td colspan="6">No tests found.</td></tr>'}
            </tbody>

        </table>

    </div>

</section>


<footer>
    QA AUTOMATION DASHBOARD
    · Generated: {generated}
    · Total test duration: {total_duration:.2f} seconds
</footer>

</div>

</body>
</html>
"""


# Crear carpeta si no existe y guardar dashboard
HTML_FILE.parent.mkdir(parents=True, exist_ok=True)
HTML_FILE.write_text(html_content, encoding="utf-8")

print("\nDashboard generado correctamente:")
print(HTML_FILE)

print(
    f"Tests: {total} | Passed: {passed} | "
    f"Failed: {failed} | Skipped: {skipped}"
)

print(f"Duración total de tests: {total_duration:.2f} segundos")
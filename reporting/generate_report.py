
import json
import html
import logging

from pathlib import Path
from datetime import datetime


# ============================================================
# CONFIGURACION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

REPORTS_DIR = BASE_DIR / "reports"
JSON_FILE = REPORTS_DIR / "results.json"
HTML_FILE = REPORTS_DIR / "report.html"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)


# ============================================================
# LECTURA DE RESULTADOS
# ============================================================

def load_results():

    if not JSON_FILE.exists():
        raise FileNotFoundError(
            f"No se encuentra el archivo de resultados: {JSON_FILE}. "
            "Ejecuta primero los tests de Pytest."
        )

    with JSON_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def get_outcome(test):
    return test.get("outcome", "unknown").lower()


def get_duration(test, phase):
    phase_data = test.get(phase, {})
    return float(phase_data.get("duration", 0) or 0)


def get_total_duration(test):
    return sum(
        get_duration(test, phase)
        for phase in ("setup", "call", "teardown")
    )


def get_error_details(test):

    error_details = []

    for phase in ("setup", "call", "teardown"):
        phase_data = test.get(phase, {})
        crash = phase_data.get("crash", {})

        message = crash.get("message")

        if message:
            error_details.append(
                f"{phase.upper()}: {message}"
            )

    return error_details


# ============================================================
# GENERACION DE ESTADISTICAS
# ============================================================

def generate_statistics(tests):

    passed = sum(get_outcome(test) == "passed" for test in tests)
    failed = sum(get_outcome(test) == "failed" for test in tests)
    skipped = sum(get_outcome(test) == "skipped" for test in tests)
    errors = sum(get_outcome(test) == "error" for test in tests)

    total = len(tests)

    pass_rate = round(
        (passed / total) * 100, 1
    ) if total else 0

    total_duration = sum(
        get_total_duration(test) for test in tests
    )

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "errors": errors,
        "pass_rate": pass_rate,
        "total_duration": total_duration
    }


# ============================================================
# GENERACION DE FILAS HTML
# ============================================================

def generate_table_rows(tests):

    rows = []

    for test in tests:

        nodeid = html.escape(
            test.get("nodeid", "Unknown test")
        )

        outcome = get_outcome(test)

        allowed_statuses = (
            "passed", "failed", "skipped", "error"
        )

        status_class = (
            outcome if outcome in allowed_statuses else "unknown"
        )

        total_time = get_total_duration(test)

        setup_time = get_duration(test, "setup")
        call_time = get_duration(test, "call")
        teardown_time = get_duration(test, "teardown")

        error_details = get_error_details(test)

        error_html = ""

        if error_details:
            error_text = html.escape(
                "\n".join(error_details)
            )

            error_html = f"""
                <details class="error-details">
                    <summary>Ver error</summary>
                    <pre>{error_text}</pre>
                </details>
            """

        rows.append(f"""
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
        """)

    if not rows:
        return '<tr><td colspan="6">No tests found.</td></tr>'

    return "\n".join(rows)


# ============================================================
# GENERACION DE GRAFICAS DE DURACION
# ============================================================

def generate_duration_bars(tests):

    if not tests:
        return "<p>No test data available.</p>"

    max_duration = max(
        (get_total_duration(test) for test in tests),
        default=0
    ) or 1

    bars = []

    for test in tests:

        name = html.escape(
            test.get("nodeid", "Unknown test")
        )

        seconds = get_total_duration(test)

        width = min(
            (seconds / max_duration) * 100, 100
        )

        outcome = get_outcome(test)

        if outcome == "passed":
            color = "#34d399"
        elif outcome in ("failed", "error"):
            color = "#f87171"
        else:
            color = "#fbbf24"

        bars.append(f"""
            <div class="bar-item">
                <div class="bar-label">
                    <span>{name}</span>
                    <strong>{seconds:.2f} s</strong>
                </div>
                <div class="bar-track">
                    <div class="bar-fill"
                         style="width:{width:.2f}%;background:{color}">
                    </div>
                </div>
            </div>
        """)

    return "\n".join(bars)


# ============================================================
# CONSTRUCCION DEL DASHBOARD
# ============================================================

def generate_html(report):

    tests = report.get("tests", [])

    stats = generate_statistics(tests)

    rows = generate_table_rows(tests)
    bars = generate_duration_bars(tests)

    generated = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

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
        #34d399 0% {stats["pass_rate"]}%,
        #f87171 {stats["pass_rate"]}% 100%
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
        <h2>{stats["total"]}</h2>
    </div>

    <div class="card">
        <span>PASSED</span>
        <h2 class="green">{stats["passed"]}</h2>
    </div>

    <div class="card">
        <span>FAILED / ERRORS</span>
        <h2 class="red">{stats["failed"] + stats["errors"]}</h2>
    </div>

    <div class="card">
        <span>PASS RATE</span>
        <h2 class="green">{stats["pass_rate"]}%</h2>
    </div>

    <div class="card">
        <span>TOTAL DURATION</span>
        <h2 class="blue">{stats["total_duration"]:.2f} s</h2>
    </div>

</section>

<section class="panels">

    <div class="panel">
        <h3>Test results distribution</h3>

        <div class="chart">

            <div class="donut">
                <div class="donut-inner">
                    <strong>{stats["pass_rate"]}%</strong>
                    <small>PASS RATE</small>
                </div>
            </div>

            <div class="legend">
                <div>
                    <span class="dot" style="background:#34d399"></span>
                    Passed: {stats["passed"]}
                </div>

                <div>
                    <span class="dot" style="background:#f87171"></span>
                    Failed: {stats["failed"]}
                </div>

                <div>
                    <span class="dot" style="background:#fbbf24"></span>
                    Skipped: {stats["skipped"]}
                </div>

                <div>
                    <span class="dot" style="background:#a78bfa"></span>
                    Errors: {stats["errors"]}
                </div>
            </div>

        </div>
    </div>

    <div class="panel">
        <h3>Test execution duration</h3>
        {bars}
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
                {rows}
            </tbody>

        </table>

    </div>

</section>

<footer>
    QA AUTOMATION DASHBOARD
    · Generated: {generated}
    · Total test duration: {stats["total_duration"]:.2f} seconds
</footer>

</div>

</body>
</html>
"""

    return html_content


# ============================================================
# EJECUCION PRINCIPAL
# ============================================================

def main():

    try:
        report = load_results()

        html_content = generate_html(report)

        REPORTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        HTML_FILE.write_text(
            html_content,
            encoding="utf-8"
        )

        stats = generate_statistics(
            report.get("tests", [])
        )

        logging.info("Dashboard generado correctamente.")
        logging.info("Archivo: %s", HTML_FILE)
        logging.info(
            "Tests: %s | Passed: %s | Failed: %s | Skipped: %s",
            stats["total"],
            stats["passed"],
            stats["failed"],
            stats["skipped"]
        )
        logging.info(
            "Duracion total: %.2f segundos",
            stats["total_duration"]
        )

    except (FileNotFoundError, json.JSONDecodeError, OSError) as error:
        logging.error("%s", error)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())